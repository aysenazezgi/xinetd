#!/usr/bin/env python
import sys
import hashlib
import os.path
import logging
#from __future__ import print_function



logging.basicConfig(filename='/home/aysenazezgi/Desktop/xinetd_hw.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

path = "/home/aysenazezgi/Desktop/myServer/"
buf = sys.stdin.readline().strip()
if len(buf):
	buflist = buf.split('#')
	file_name = buflist[0]
	clientmd5 = buflist[1]
	data = buflist[2]
	f = open(path + file_name, 'w+')
	f.write(data)
	f.close()
	logging.info("file transfer begin")
	print ("File transfer begin\n *******\n\n")
	md5local = md5(path + file_name)
	logging.info("Calculated md5 server :%s",md5local)
	if md5local == clientmd5:
		logging.info("Calculated md5s are equal")
		print 'Server md5  :  '+ md5local
		print '\n File transfer is successfull\n'
		logging.info("File transfer is successful")
	else:
		print 'Server md5  :  '+ md5local
		logging.debug("md5s are not equal.")
		print '\nFile transferred but not successfull\n'
		logging.warning("File transferred but not successful")
	print("\n-----Server Disconnected-----\n***\n")
	sys.stdout.flush().strip()

