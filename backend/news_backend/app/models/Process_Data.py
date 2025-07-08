from app import db
from sqlalchemy import or_, text
from app.models.device_properties import DeviceProperties

def get_latest_electrical_params():
    query = text("""
        SELECT dp.* 
        FROM device_properties dp
        INNER JOIN (
            SELECT device_id, MAX(event_time) as max_time
            FROM device_properties
            GROUP BY device_id
        ) latest ON dp.device_id = latest.device_id AND dp.event_time = latest.max_time
    """)
    return db.session.query(DeviceProperties).from_statement(query).all()
