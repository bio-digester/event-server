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
        sensor = session.query(SensorSchema).filter(SensorSchema.name == name).one()
        session.close()
        self._dispose()
        return sensor 

class DataCollect(Database):
    
    def __init__(self):
        super().__init__()
    
    def set_value(self, sensor, sensor_value):
        data_collect = DataCollectSchema(data_measure=datetime.now(), 
            value=sensor_value, sensor_id=sensor.id)
        session = self._create_engine()
        session.add(data_collect)
        session.commit()
        session.close()
        self._dispose()

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
        session.close()
        self._dispose()

    def all(self):
        session = self._create_engine()
        notifications = session.query(NotificationSchema).all() 
        session.close()
        self._dispose()
        return notifications
