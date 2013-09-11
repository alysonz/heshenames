#!/usr/bin/env python
#reformat and label names
import re
doanames = open('doanames.txt', 'r')
doanames = doanames.readlines()
femnames = open('femnames.txt', 'r')
femnames = femnames.readlines()
doa = []
for line in doanames:
	line = re.sub('\n','',line)
	#make a list of doa names
	doa.append(line)
doa = [element.upper() for element in doa]
names = []
for line in femnames:
	line = re.sub('\n','',line)
	#make a list female names and stats
	names.append(line)
#set list position of female names to the first name/stat
d = 0
#make list for writing to a file
fememp = []

#re.search is clearly not what I want to use here

#take a name in doa
for item in doa:
	#search for that name within each list item of female names
	#while there is no match within that list item, add 1 to list position variable and do it again
	while re.search(item, names[d])== None:
	#as long as the list item is not the last item in the list, add one and check the next female name/stat
		if names[d] != names[-1]:
			d=d+1
	#if we have reached the end of the name/stats to check, will return none, if match return names[d]
		elif re.search(item, names[d])== None:
			item = 'None'
		else:
			item = item + ", " + names[d]
	fememp.append(item)
doafem = open('doafem.txt','w')
doafem.writelines(fememp)
