#!/usr/bin/env python
#reformat and label names
import re
emp = open('doa13.txt', 'r')
emp = emp.readlines()
names = []
for line in emp:
	#find first comma, get rid of all text preceeding it
	#line = re.sub('.*	','%s',line, count=1)%(
	pattern = re.compile('.*,')
	re.match(pattern, line)
	#find first tab or space, get rid of all text following it
#	names.append(line)
#empnames = open('doafull.txt','w')
#empnames.writelines(names)
