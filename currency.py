#!/usr/bin/env python
#reformat and label names
import re
emp = open('doa12.txt', 'r')
emp = emp.readlines()
names = []
for line in emp:
	#find first comma, get rid of all text preceeding it
	line = re.sub('\$','',line)
	#find first tab or space, get rid of all text following it
	names.append(line)
empnames = open('doafull12.txt','w')
empnames.writelines(names)
