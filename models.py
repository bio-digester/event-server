from datetime import datetime
from database import Database
from schema import Sensor as SensorSchema, DataCollect as DataCollectSchema

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

    def aaa(self):
        session = self._create_engine()
        return session.query(DataCollectSchema).first()
        
