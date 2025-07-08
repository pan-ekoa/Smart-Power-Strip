from flask import request, Blueprint, jsonify
from app.models.Process_Data import get_latest_electrical_params
from app.utils.common import api_response

from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials

control_bp = Blueprint('StripControl', __name__)

@control_bp.route('/', methods=['POST'])
def Control_Strip():
    data = request.json
    print(data)
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
