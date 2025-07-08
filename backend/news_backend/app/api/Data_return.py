from flask import request, Blueprint, jsonify
from app.models.Process_Data import get_latest_electrical_params
from app.utils.common import api_response

import time
import json


Datareturn_bp = Blueprint('home', __name__)

@Datareturn_bp.route('/index', methods=['GET'])
def get_latest_electrical():
    devices = get_latest_electrical_params()
    json_data = jsonify([{
        'DeviceID': d.device_id,
        'Voltage': d.voltage,
        'Current': d.current,
        'Power': d.power,
        'Energy': d.electricity,
        'Status': d.control_signal,
        'Time': d.event_time.isoformat() if d.event_time else None
    } for d in devices])
    return api_response(True,"success",json_data)
