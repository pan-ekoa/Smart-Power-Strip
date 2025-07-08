from flask import request, Blueprint, jsonify
from app.models.Process_Data import get_latest_electrical_params
from app.utils.common import api_response

control_bp = Blueprint('command', __name__)

@control_bp.route('/', methods=['GET'])
def Control_Strip():
    device_id = request.args.get('id')
    signal = request.args.get('status')
    print(device_id, signal)
    return api_response(True, "success")
