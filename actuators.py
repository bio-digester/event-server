import socket
from database import *

class Actuators(object):
    def __init__(self):
        self.resistence = 0
        self.mixer = 0
        self.gas_passage = 0

    def __send(self, port, message):
        # While don't have actuator code
        # actuatorsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # actuatorsock.connect(('127.0.0.1', port))
        # actuatorsock.sendall(message)
        pass

    def verify(self, sensors):
        if(sensors['TEMPDS'] < 30):
            self.__workResistence(1)
        else:
            self.__workResistence(0)

    def __workResistence(self, status):
        if(status != self.resistence):
            # send change to actuator code 
            print("Changing Resistence to ", status)    
            self.__send(6550, status)
            self.resistence = status


