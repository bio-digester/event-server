from datetime import datetime
from database import Database
from schema import Sensor as SensorSchema
from schema import DataCollect as DataCollectSchema
from schema import Notification as NotificationSchema


class Sensor(Database):
    
    def __init__(self):
        super().__init__()

    def get_sensor(self, name):
        session = self._create_engine()

        return session.query(SensorSchema).filter(SensorSchema.name == name).one()

class DataCollect(Database):
    
    def __init__(self):
        super().__init__()
    
    def set_value(self, sensor, sensor_value):
        data_collect = DataCollectSchema(data_measure=datetime.now(), 
            value=sensor_value, sensor_id=sensor.id)
        session = self._create_engine()
        session.add(data_collect)
        session.commit()

class Notification(Database):       
    
    def __init__(self):
        super().__init__()
        self.MIN_LEVEL = 5000
        self.MAX_LEVEL = 40000
        self.SEC_PRESSURE = 10
        self.WARNING_PRESSURE = 20

    def send_message(self, msg):
        notification = NotificationSchema(message_date=datetime.now(), message=msg)
        session = self._create_engine()
        session.add(notification)
        session.commit()

    def all(self):
        session = self._create_engine()
        
        return session.query(NotificationSchema).all()
