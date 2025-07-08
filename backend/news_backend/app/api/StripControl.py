from flask import request, Blueprint, jsonify
from app.models.Process_Data import get_latest_electrical_params
from app.utils.common import api_response

control_bp = Blueprint('command', __name__)

@control_bp.route('/', methods=['POST'])
def Control_Strip():
    data = request.json
    print(data)
    return api_response(True, "success")
