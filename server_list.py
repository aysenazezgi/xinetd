#!/usr/bin/env python
from os import listdir,mkdir
from os.path import isfile, join, exists 
import sys
import logging


logging.basicConfig(filename='/home/aysenazezgi/Desktop/xinetd_hw.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

while True:
	path = "/home/aysenazezgi/Desktop/myServer"
	print ("\n--------Connected-------")
	if exists(path):
		print ("Server directory found")
		print ("\nServer Directory\n")
		list = [f for f in listdir(path) if isfile(join(path,f))]
		if len(list)==0:
			logging.info("Server directory created but empty")
			print("\nServer Directory is created but empty.\n")
		else :
			logging.info("Server directory includes %s",list)
			print list
	else :
		mkdir(path)
		logging.debug("There is no Server directory")
		if exists (path):
			logging.info("Server directory created")
			print ("\nData Directory is created\n")
		else :
			logging.error("Error occur while creating directory")
			print ("Error")
	sys.stdout.flush()
	logging.info("Disconnect server")
	break
