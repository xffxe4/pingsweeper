#!/usr/bin/python
#
###############################################
# Simple local subnet ping sweeper 
# Author: bravobingomazinga@gmail.com
# Version: 0.1 (Last updated 2016-07-11)
###############################################
#

import os
import re
import sys

showline = re.compile(r"(\d) received")
verdict = ("Offline","Online","Alive")

# ping sweep of the local C class subnet 10.0.1.0/24 
for host in range(1,254):
	ip = "10.1.1."+str(host)
	shootping = os.popen("ping -c 1 "+ip, "r")
	print ip,
	sys.stdout.flush()
	while 1:
		line = shootping.readline()
		if not line:break
		outcome = re.findall(showline, line)
		if outcome:
			print verdict[int(outcome[0])]

