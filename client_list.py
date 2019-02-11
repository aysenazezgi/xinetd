import socket
import sys
import logging


logging.basicConfig(filename='/home/aysenazezgi/Desktop/xinetd_hw.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
message = '1'
server_address = ('10.0.2.15', 4444)
s.connect(server_address)
logging.info("Server connected")
logging.info("Request send to Server")
s.send(message)
s.shutdown(socket.SHUT_WR)
data = s.recv(1024)
print data
s.close()
print ("\n----Disconnected Server ----\n")

