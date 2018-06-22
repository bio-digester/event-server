import socket
import threading
import socketserver
import time
from actuators import *
from sensors import Sensors

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        if(len(data) < 3):
            return
        print("#####>>> ", data)

        sensor, value = data.split()

        if(sensor == 'REMOVE'):
            sensors.gas(value)
        elif(sensor != 'ENTRY' and sensor != 'LEVEL'):
            print('[server] Get sensor\'s id in database')
            current_sensor = sensors.get_sensor(sensor)
            sensors.work(current_sensor, value)
        else:
            if(sensor == 'ENTRY'):
                print('[server] Food actions')
                current_sensor = None       
            else:        
                current_sensor = sensors.get_sensor(sensor)
            sensors.work(current_sensor, value)
            actuators.entry(sensors.sensors, current_sensor)
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
    SECURITY_HOST, SECURITY_PORT1, SECURITY_PORT2 = "127.0.0.1", 7000, 7001
    while True:

#        # security 1 pulse
#        security_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        security_tcp.connect((SECURITY_HOST, SECURITY_PORT1))
#        security_tcp.sendall(b'SERVER')
#
#        # security 2 pulse
#        security_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        security_tcp.connect((SECURITY_HOST, SECURITY_PORT1))
#        security_tcp.sendall(b'SERVER')
        time.sleep(5)
