from app import db

class DeviceProperties(db.Model):
    __tablename__ = 'device_properties'

    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=False)
    voltage = db.Column(db.Float, nullable=False)
    current = db.Column(db.Float, nullable=False)
    power = db.Column(db.Float, nullable=False)
    electricity = db.Column(db.Float, nullable=False)
    control_signal = db.Column(db.Boolean, nullable=False)
    event_time = db.Column(db.DateTime, nullable=False)
    record_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __repr__(self):
        return f"<DeviceProperties {self.device_id} {self.event_time}>"
