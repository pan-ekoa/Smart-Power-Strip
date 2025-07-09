from flask import request, Blueprint, jsonify
from app.models.Process_Data import get_latest_electrical_params
from app.utils.common import api_response
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials
from app.client import client
import json
control_bp = Blueprint('command', __name__)

@control_bp.route('/', methods=['GET'])
def Control_Strip():
    device_id = request.args.get('id')
    signal = request.args.get('status')
    print(device_id, signal)
    
    request1 = CreateCommandRequest()
    request1.device_id = "6868dfca32771f177b490743_0001"
    commandjson = {
        "Signal": signal,
        "DeviceID": device_id
    }
    request1.body = DeviceCommandRequest(
        paras=commandjson,
            command_name="Control",
            service_id="environment"
    )

    client.create_command(request1)
    return api_response(True, "success")

@control_bp.route('/time', methods=['GET'])
def Control_Strip_time():
    device_id = request.args.get('id')
    time = request.args.get('time')
    print(device_id, time)
    return api_response(True, "success")