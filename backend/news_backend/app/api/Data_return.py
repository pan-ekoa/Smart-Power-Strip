from flask import request, Blueprint, jsonify
from app.models.Process_Data import get_latest_electrical_params, get_60_electrical
from app.utils.common import api_response
from app.models.InvokeAPI import DEEPSEEK_API
import time
import json


Datareturn_bp = Blueprint('device', __name__)

@Datareturn_bp.route('/', methods=['GET'])
def get_latest_electrical():
    device_id = request.args.get('id')
    devices = get_latest_electrical_params()
    if device_id:
        devices = [d for d in devices if str(d.device_id) == device_id]
        if not devices:
            return api_response(False, "Device not found", None, 404)
    
    data = [{
        'DeviceID': d.device_id,
        'Voltage': d.voltage,
        'Current': d.current,
        'Power': d.power,
        'Energy': d.electricity,
        'Status': int(d.control_signal),
        'Time': d.event_time.isoformat() if d.event_time else None
    } for d in devices]
    return api_response(True, "success", data[0])

@Datareturn_bp.route('/strip', methods=['GET'])
def get_electrical_60():
    device_id = request.args.get('id')
    devices = get_60_electrical()
    
    if device_id:
        devices = [d for d in devices if str(d.device_id) == device_id]
        if not devices:
            return api_response(False, "Device not found", None, 404)
    data = {
        'voltage': [d.voltage for d in devices],
        'current': [d.current for d in devices],
        'power': [d.power for d in devices],
        'energy': [d.electricity for d in devices],
        'time': [d.event_time.isoformat() if d.event_time else None for d in devices]
    }
    return api_response(True, "success", data)

@Datareturn_bp.route('/advice', methods=['GET'])
def get_advice():
    content = DEEPSEEK_API()
    data = {
        'message' : content
    }
    return api_response(True, "success", data)