from flask import jsonify
from app import db
import os
from werkzeug.utils import secure_filename
import tempfile
import datetime
from dotenv import load_dotenv
from app.utils.time_util import china_time_now

# 加载环境变量
load_dotenv()

def api_response(success=True, message="", data=None, status_code=200):
    """统一API响应格式"""
    return jsonify({
        "success": success,
        "message": message,
        "data": data
    }), status_code
