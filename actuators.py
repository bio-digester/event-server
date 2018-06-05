import socket
import time
from database import *

class Actuators(object):
    resistence = 0
    mixer = 0
    gas_passage = 0

    def __send(self, port, message):
        # While don't have actuator code
        actuatorsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        actuatorsock.connect(('127.0.0.1', port))
        actuatorsock.sendall(str(message).encode())
        # pass

    def verify(self, sensors):
        print("[actuators] last sensors data ", sensors)
        # temperature
        if(sensors['TEMPDS'] < 30):
            self.__workResistence(1)
        else:
            self.__workResistence(0)
        if(sensors['PRESSURE'] < .5):
            self.__workGasPassage(1)
        else:
            self.__workGasPassage(0)


    def entry(self, sensors, current):
        if(current == 'LEVEL' and sensors['ENTRY']['status'] == 0 and
            sensors['ENTRY']['level'] != 0 and self.mixer == 0):
            total_water = sensors['LEVEL'] - sensors['ENTRY']['level']
            print("[actuators] Sending water value: ", total_water)
            self.__send(6553, total_water)
            sensors['ENTRY']['level'] = 0
        elif(current == 'ENTRY'):
            if(sensors['ENTRY']['status'] == 1):
                self.mixer = 1
                print("[actuators] Turn on mixer")
                self.__send(6551, 1) # turn on mixer
            else:
                self.__workWater(sensors)

    def __workResistence(self, status):
        if(status != self.resistence):
            # send change to actuator code 
            print("[actuators] Changing Resistence to ", status)    
            self.__send(6550, status)
            self.resistence = status

    def __workWater(self, sensors):
            # Turn off mixer
            time.sleep(5)
            print("[actuators] Turn off mixer")
            self.__send(6551, 0) # turn off mixer
            self.mixer = 0

    def __workGasPassage(self, status):
        if(status != self.gas_passage):
            # send change to actuator code 
            print("[actuators] Changing gás passage to ", status)    
            self.__send(6552, status)
            self.gas_passage = status
