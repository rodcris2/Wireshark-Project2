from socket import *
import random
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
while True:
    rand = random.uniform(0.01, 0.04)

    message, address = serverSocket.recvfrom(1024)
    time.sleep(rand)

    serverSocket.sendto(message, address)