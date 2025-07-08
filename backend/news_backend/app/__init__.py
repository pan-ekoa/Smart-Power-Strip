from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

# 初始化Flask应用
app = Flask(__name__)
CORS(app)
# print("MAIL_PASSWORD from env:", os.environ.get("MAIL_PASSWORD"))

# 配置数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ly85190316,@127.0.0.1:3306/device_monitoring'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 这个不关会有警告！
db = SQLAlchemy(app)

from app.api.auth import auth
app.register_blueprint(auth, url_prefix='/auth')

from app.api.Data_return import Datareturn_bp
app.register_blueprint(Datareturn_bp, url_prefix='/device')

from app.api.StripControl import control_bp
app.register_blueprint(control_bp, url_prefix='/command')
