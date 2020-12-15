from subprocess import call
import time
import os

while True:
	print("Starting new sess")
	
	os.system("lxterminal -e mef_retriever.py")
	time.sleep(3600)
