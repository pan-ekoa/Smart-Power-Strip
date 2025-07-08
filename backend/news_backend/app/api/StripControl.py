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
    return api_response(True, "success")
