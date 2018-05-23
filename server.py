import socket
import threading
import socketserver
import time
from actuators import *
from sensors import *

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        sensor, value = data.split()

        if(sensor != 'ENTRY' and sensor != 'LEVEL'):
            print('[server] Get sensor\'s id in database')
            current_sensor = sensors.getSensor(sensor)
            sensors.work(current_sensor, value)
        else:
            if(sensor == 'ENTRY'):
                print('[server] Food actions')
                current_sensor = {}        
                current_sensor[1] = 'ENTRY'
            else:        
                current_sensor = sensors.getSensor(sensor)
            sensors.work(current_sensor, value)
            actuators.entry(sensors.sensors, current_sensor[1])
        actuators.verify(sensors.sensors)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

sensors = Sensors()
actuators = Actuators()

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 6500

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server running")

    # run the parent process indefinitely
    while True:
        time.sleep(1)

