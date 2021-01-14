#!/usr/bin/python3
from subprocess import call
import time
import os

while True:
	print("Starting new session")
	os.system("lxterminal -e python3 mef_retriever.py")
	#os.system("python3 mef_retriever.py")
	#time.sleep(30)
	time.sleep(3600)
