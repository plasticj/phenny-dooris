#!/usr/bin/env python
"""
dooris.py - Phenny DoorisModule
by plasticj
"""
import urllib
from datetime import datetime

def mex(phenny, input):
	h = urllib.urlopen("http://dooris.koalo.de/door.txt")	
	lines = h.readlines()

	t1 = int(lines[1].strip())
	t2 = int(lines[2].strip())

	dt1 = datetime.fromtimestamp(t1) # update
	dt2 = datetime.fromtimestamp(t2) # change 

	phenny.say(lines[0].strip() + " seit " + dt2.isoformat(' ') + ". Letztes Update " + dt1.isoformat(' '))

mex.command = ['mex']
mex.rule = r'\.mex'
mex.priority = "low"

if __name__ == '__main__': 
   print __doc__.strip()
