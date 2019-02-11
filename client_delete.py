import socket
import sys
import logging


logging.basicConfig(filename='/home/aysenazezgi/Desktop/xinetd_hw.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

message = raw_input("\nEnter file name to delete  :   ")
logging.info("User want to delete %s",message)
server_address = ('127.0.0.1', 4447)
s.connect(server_address)
s.send(message)
s.shutdown(socket.SHUT_WR)
data = s.recv(1024)
print data
s.close()
logging.info("Action is completed.")
