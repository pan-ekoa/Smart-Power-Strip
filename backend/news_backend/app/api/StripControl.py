from flask import request, Blueprint, jsonify
from app.models.Process_Data import get_latest_electrical_params
from app.models.device_settings import DeviceSettings
from app.utils.common import api_response
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials
from app.client import client
from datetime import datetime
import json
from app import db
import pytz

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
    time_str = request.args.get('time')
    print(device_id, time_str)
    try:
        # 转换时间字符串为datetime对象
        dt = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
        london_time = dt.replace(tzinfo=pytz.UTC)
    
    # 3. 转换为北京时间（UTC+8）
        beijing_tz = pytz.timezone('Asia/Shanghai')
        beijing_time = london_time.astimezone(beijing_tz)
        # 创建并保存设备设置记录
        new_setting = DeviceSettings(
            device_id=device_id,
            set_time=beijing_time.strftime("%Y-%m-%d %H:%M:%S"),
            record_time=datetime.now()  # 记录当前时间
        )
        db.session.add(new_setting)
        db.session.commit()
        
        return api_response(True, "Device setting saved successfully")
    except ValueError as e:
        return api_response(False, f"Invalid time format: {str(e)}", None, 400)
    except Exception as e:
        db.session.rollback()
        return api_response(False, f"Failed to save device setting: {str(e)}", None, 500)
