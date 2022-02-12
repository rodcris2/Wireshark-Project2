from socket import *
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

serverSocket.settimeout(10)

while True:
    try:
        start = time.time()

        message, address = serverSocket.recvfrom(1024)
        end = time.time()

        elapsed = end - start
        print('Server received ' + message.decode('utf-8') + ' Pulse interval was ' + format(round(elapsed)) + ' seconds')
    except timeout:
        print('No pulse after 10 seconds. Server quits.')
        break
print('Server stops.')