#!/usr/bin/python
from os import listdir
from os.path import isfile, join,exists
from os import remove as rmfile
import sys


logging.basicConfig(filename='/home/aysenazezgi/Desktop/xinetd_hw.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

print ("\n-----Server Connected----\n")
logging.info("Server connected")

path = "/home/aysenazezgi/Desktop/myServer/"
buf = sys.stdin.readline().strip()
retval = -1
control1=True
control2=True
if len(buf):
	for f in listdir(path):
		logging.info("Checking if there is%s",buf)
		fullpath=path+f
		if isfile(fullpath):
			if f == buf:
				rmfile(fullpath)
				retval = '\nFile is Deleted\n'
				print retval
				control1=False
				break;
		#elif exists(fullpath):
			#print ("\n***Exists but this is not a file ***\n")
			#control2=False
			#break
if retval != 0:
	retval = -1
if control1 and control2:
	logging.error("File does not exists or some error occured")
	print '\n***File does not exists or some error occured***\n'

print ("\n-----Server Disconnected------\n")
logging.info("Server disconnected")
sys.stdout.flush().strip()
