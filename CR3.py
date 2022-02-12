from socket import *
import random
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
while True:
    rand = random.uniform(0.01, 0.04)
    loss = random.uniform(0, 1)

    message, address = serverSocket.recvfrom(1024)
    time.sleep(rand)

    if loss <= 0.20:
        continue
    serverSocket.sendto(message, address)