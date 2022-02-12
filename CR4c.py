import time
from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ('127.0.0.1', 12000)

i = 1
while True:
    msg = 'heartbeat pulse ' + str(i)
    print(msg)
    clientSocket.sendto(msg.encode('utf-8'), serverAddress)
    i += 1
    time.sleep(5)