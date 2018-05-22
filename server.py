import socket
import threading
import socketserver
import time
from database import *
from actuators import *

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        database = Database()
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        sensor, value = data.split()

        print('Get sensor\'s id in database')
        for sensor in database.getSensorByName(sensor):
            print(sensor)
        
        print('Try insert ', sensor[1])
        database.setValue(sensor[0], value)
        print('Inserted ', sensor[0], ' -- Value: ', value)
        actuators.verify(database.getLastSensorsValues())

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

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

