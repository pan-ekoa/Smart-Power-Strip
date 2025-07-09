from app import db
from datetime import datetime

class DeviceSettings(db.Model):
    __tablename__ = 'device_settings'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(255), nullable=False)
    set_time = db.Column(db.DateTime, nullable=False)
    record_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, device_id, set_time, record_time):
        self.device_id = device_id
        self.set_time = set_time
        self.record_time = record_time
