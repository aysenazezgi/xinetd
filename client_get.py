import socket
import sys
import hashlib
import os.path
import logging


logging.basicConfig(filename='/home/aysenazezgi/Desktop/xinetd_hw.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')


logging.info("Program Starts")

def md5(filename):
	hash_md5 = hashlib.md5()
	with open(filename, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
path = "/home/aysenazezgi/Desktop/myClient/"
message = raw_input()
fullpath= path + message
s.connect(('127.0.0.1', 4445))
print ("\n-----Server Connected-----\n")
s.send(message)
s.shutdown(socket.SHUT_WR)
data = s.recv(32)
md5fromserver = data 
generaldata = "" 
print 'MD5 : ' + md5fromserver
while data:
	data = s.recv(1024)
	generaldata += data

generaldata=generaldata[len(md5fromserver)+1:]

s.close()
logging.info("Server Disconnected")
print ("\n----Server Disconnected----\n")

if(md5fromserver.strip() != "error"):
	f = open(fullpath,"w+")
	f.write(generaldata)
	f.close()
	logging.info("Local md5 calculating")
	md5local = md5(fullpath)
	print 'Calculated MD5: ' +  md5local
	logging.info("Local md5 is %s for %s",md5local,message)
	if md5fromserver == md5local:
		logging.info("md5 form server and client are equal")
		print '\nFile transferred!\nYou can find your file as  '+fullpath+ '\n'
		logging.info("File transferred to client succesfully")
	else:
		print '\nFile transferred but not correctly\n:(\n'
		logging.info ("File transferred but not correctly")
logging.info("Program finishes")
