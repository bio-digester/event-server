import socket
from models import Sensor, DataCollect, Notification

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
            if(sensor.name == 'LEVEL'):
               value = float(value) / 1000.0
            print("[sensors] SAVING: ", sensor.codename, " value: ", value)
 
            data_collect_db = DataCollect()
            data_collect_db.set_value(sensor, value)
            self.__notification()
        else:
            self.sensors['ENTRY']['status'] = int(value)
            if(int(value) == 1):
                self.sensors['ENTRY']['level'] = self.sensors['LEVEL']

    def __notification(self):
        notification = Notification()
        if(self.sensors['LEVEL'] < notification.MIN_LEVEL):
            notification.send_message('O nível de alimentação está abaixo do mínimo')
        elif(self.sensors['LEVEL'] > notification.MAX_LEVEL):            
            notification.send_message('O nível de alimentação está no limite, retire o biofertilizante')
        if(self.sensors['PRESSURE'] > notification.SEC_PRESSURE and
            self.sensors['PRESSURE'] < notification.WARNING_PRESSURE):
            notification.send_message('O biogás está pronto para ser retirado')
        elif(self.sensors['PRESSURE'] > notification.WARNING_PRESSURE):            
            notification.send_message('Retire urgentemente o biogás')

        print(notification.all())            
        

