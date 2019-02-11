#!/usr/bin/env python
import sys
import hashlib
import time
import os.path
import logging
from shutil import copyfile

#from __future__ import print_function

logging.basicConfig(filename='/home/aysenazezgi/Desktop/xinetd_hw.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')


logging.info("Server connected")

def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()
try:
	path = "/home/aysenazezgi/Desktop/myServer/"
	data = b""
	while True:
		buf = sys.stdin.readline()
		buf=buf.replace("\n","")
		if len(buf):
			fullpath= path + buf 
			if os.path.isfile(fullpath):
				logging.info("File found in server %s" ,fullpath)
				md5 = md5(fullpath)
				data = md5
				print (data)
				f = open(fullpath,'rb')
				l = f.read(1024)
				l = l.strip('\n')
				length = len(l)
				logging.info("File transfer begin")
				while (l):
					data += l
					l = f.read(1024)
				f.close()
				print data
				logging.info("File transfer is finished")
				sys.stdout.flush()
			else: 
				logging.debug("File can not be found or not file.")
				print 'error'
				sys.stdout.flush()
		copyfile('/home/aysenazezgi/Desktop/xinetd_hw.log',path)
		copyfile('/home/aysenazezgi/Desktop/xinetd_hw.log',"/home/aysenazezgi/Desktop/myClient/")
		break
except Exception as ex:
	logging.ERROR(str(ex))

