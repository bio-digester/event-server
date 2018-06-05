import socket
from models import Sensor, DataCollect

class Sensors(object):
    def __init__(self):
        self.sensors = {}
        self.sensors['TEMPDS'] = 0
        self.sensors['PRESSURE'] = 0
        self.sensors['PH'] = 0
        self.sensors['CONCENTRATION'] = 0
        self.sensors['LEVEL'] = 0
        self.sensors['ENTRY'] = {}
        self.sensors['ENTRY']['status'] = 0
        self.sensors['ENTRY']['level'] = 0

    def get_sensor(self, sensor):
        sensor_db = Sensor()
        return sensor_db.get_sensor(sensor) 

    def work(self, sensor, value):
        if(sensor != None):
            self.sensors[sensor.name] = float(value)
            print("[sensors] SAVING: ", sensor.codename, " value: ", value)
 
            data_collect_db = DataCollect()
            data_collect_db.set_value(sensor, value)
        else:
            self.sensors['ENTRY']['status'] = int(value)
            if(int(value) == 1):
                self.sensors['ENTRY']['level'] = self.sensors['LEVEL']
