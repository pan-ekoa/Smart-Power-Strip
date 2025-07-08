from flask import request, Blueprint, jsonify
from app.models.Process_Data import get_latest_electrical_params
from app.utils.common import api_response

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
