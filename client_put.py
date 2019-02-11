import socket
import sys
import hashlib
import os.path
import logging


logging.basicConfig(filename='/home/aysenazezgi/Desktop/xinetd_hw.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()


path = "/home/aysenazezgi/Desktop/myClient/"
data = b""
file_name = raw_input("\nEnter file name   :  ")
logging.info("Client want to put %s to server",file_name)
if os.path.isfile(path + file_name):
	logging.info("File is found")
	md5 = md5(path + file_name)
	print '\nClient md5  :  '+md5+"\n"
	logging.info("md5 of file is %s",md5)
	f = open(path + file_name, 'rb')
	l = f.read(1024)
	l = l.strip('\n')
	while(l):
		data += l.strip('\n')
		l = f.read(1024)
	f.close()
	message = file_name + '#' + md5 + '#' + data 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', 4446))
	print ("\n-----Server Connected-----\n")
	s.send(message)
	s.shutdown(socket.SHUT_WR)
	back = s.recv(1024)
	s.close()
	print back.strip()
else:
	logging.error("File does not exists")
	print 'File does not exist in folder!'
