import socket
from database import *

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

    def getSensor(self, sensor):
        database = Database()
        return database.getSensorByName(sensor)[0] 

    def work(self, sensor, value):
        print("[sensors] RECEIVED: ", sensor)

        database = Database()
        if(sensor[1] != 'ENTRY'):
            self.sensors[sensor[1]] = float(value)
            print("[sensors] SAVING: ", sensor[0], " value: ", value)
            database.setValue(sensor[0], value)
        else:
            self.sensors['ENTRY']['status'] = int(value)
            if(int(value) == 1):
                self.sensors['ENTRY']['level'] = self.sensors['LEVEL']
