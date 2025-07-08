from flask import request, Blueprint, jsonify
from app.models.Process_Data import get_latest_electrical_params
from app.utils.common import api_response
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials
from app.client import client

control_bp = Blueprint('command', __name__)

@control_bp.route('/', methods=['GET'])
def Control_Strip():
    device_id = request.args.get('id')
    signal = request.args.get('status')
    print(device_id, signal)
    
    request1 = ListDevicesRequest()
    # 调用查询设备列表接口
    response = client.list_devices(request1)
    print(response)
    return api_response(True, "success")
