#!/usr/bin/env python
#reformat and label names
import re
fem = open('female.txt', 'r')
fem = fem.readlines()
names = []
for line in fem:
	#find group:s of spaces and replace them with a comma
	line = re.sub('  *','	',line)
	names.append(line)
femnames = open('femnames.txt','w')
femnames.writelines(names)
