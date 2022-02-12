from socket import *
import time

serverAddress = ('127.0.0.1', 12000)
clientSocket = socket(AF_INET, SOCK_DGRAM)
packetLoss = 0
clientSocket.settimeout(1)
RTT = []

try:
    for i in range(1,11):
        start = time.time()
        message = "seq " + str(i) + " " + time.ctime(start)
        try:
            sent = clientSocket.sendto(message.encode('utf-8'),serverAddress)
            data, address = clientSocket.recvfrom(4096)
            elapsed = format((time.time()-start)*1000, '.2f')
            RTT.append(elapsed)
            print('Ping ' + str(i) + ": host 127.0.0.1 replied: " + data.decode('utf-8') + ' RTT = ' + elapsed + (' ms'))
        except timeout:
            print('Ping ' + str(i) + ': timed out, message was lost')
            packetLoss += 1

finally:
    mean = sum(map(float,RTT))/len(RTT)-packetLoss
    print('Min RTT = ' + min(RTT) + ' ms')
    print('Max RTT = ' + max(RTT) + ' ms')
    print('Avg RTT = ' +  format(mean, '.2f') + ' ms')
    print('Packet lost = ' + format(packetLoss, '.2f') + ' %')
    clientSocket.close()