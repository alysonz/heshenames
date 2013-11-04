# General query tools
import MySQLdb
import gettuple
import re
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
dept = "you misspelled something somewhere"
highestSalary1 = "you misspelled something somewhere"
highestSalary2 = "you misspelled something somewhere"
highestSalary3 = "you misspelled something somewhere"
highestSalary4 = "you misspelled something somewhere"
highestSalary5 = "you misspelled something somewhere"
highestSalary6 = "you misspelled something somewhere"
highestSalary7 = "you misspelled something somewhere"
highestSalary8 = "you misspelled something somewhere"
highestSalary9 = "you misspelled something somewhere"
highestSalary10 = "you misspelled something somewhere"
topTen = []
hold = "you misspelled something somewhere"
placeHolder = []
remainder = []
count = []
problems = []
#create table to load data
#cursor.execute("create table generic (generic1 varchar(#), generic2 decimal (#,#), generic3 int(#))")
#find all distinct departments
cursor.execute("select distinct dept from doafull13")
for line in cursor:
	topTen = []
	hold = []
	placeHolder = []	
	remainder = []
	count = []
	dept = line
	#for each distinct department, find the highest salary in that department
	cursor.execute("select max(salary) from doafull13 where dept=%s",(dept[0]))
	highestSalary1 = gettuple.gettuple(cursor.fetchall())
	#find the employee/s with the highest salary in that department
	cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary1[0],dept[0]))
	hold = cursor.fetchall()
	#add that/those employee/s to the topTen list for that department only until topTen contains ten items, then count the remainder and append that number to topTen
	if len(hold) < 10:
		for item in hold:
			placeHolder.append(list(item))
		topTen = topTen + placeHolder
		print "1a"	
	else:
		for item in hold:
			while len(topTen) < 10:
				placeHolder = []
				count.append(list(item))
				placeHolder.append(list(item))
				topTen = topTen + placeHolder
		remainder = len(hold)-len(count)
		topTen.append(remainder)
		print "1b"
	#if there was only one employee with the top salary in that department
	if len(topTen) < 10:
		#find the second highest salary in that department
		cursor.execute("select max(salary) from doafull13 where dept=%s and salary!=%s",(dept[0],highestSalary1[0]))
		highestSalary2 = gettuple.gettuple(cursor.fetchall())
		#find the employee/s with the second highest salary in that department, but only if there was a third highest salary
		if len(highestSalary2)>0:
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary2[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department only until topTen contains ten items, then count the remainder and append that number to topTen
			if (len(topTen)+len(hold)) <= 10:
				placeHolder = []
				for item in hold:
					placeHolder.append(list(item))
				topTen = topTen + placeHolder
				print "2a"
			else:
				count = []
				remainder = []
				for item in hold:
					while len(topTen) < 10:
						placeHolder = []
						count.append(list(item))
						placeHolder.append(list(item))
						topTen = topTen + placeHolder
				remainder = len(hold)-len(count)
				topTen.append(remainder)
				print "2b"
	#if there are fewer than ten employees in the topTen list for that department
	if len(topTen) < 10:
		#find the third highest salary in that department
		cursor.execute("select max(salary) from doafull13 where dept=%s and (salary!=%s and salary!=%s)",(dept[0],highestSalary1[0],highestSalary2[0]))
		highestSalary3 = gettuple.gettuple(cursor.fetchall())
		#find the employee/s with the third highest salary in that department, but only if there was a third highest salary
		if len(highestSalary3)>0:
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary3[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department only until topTen contains ten items, then count the remainder and append that number to topTen
			if (len(topTen)+len(hold)) <= 10:
				placeHolder = []
				for item in hold:
					placeHolder.append(list(item))
				topTen = topTen + placeHolder
				print "3a"
			else:
				count = []
				remainder = []
				for item in hold:
					while len(topTen) < 10:
						placeHolder = []
						count.append(list(item))
						placeHolder.append(list(item))
						topTen = topTen + placeHolder
				remainder = len(hold)-len(count)
				topTen.append(remainder)
				print "3b"
	#if there are still fewer than ten employees in the topTen list for that department, find the fourth highest salary in that department
	if (len(topTen) < 10):
		#but only if there was a third highest salary
		if len(highestSalary3)>0:
			cursor.execute("select max(salary) from doafull13 where dept=%s and (salary!=%s and salary!=%s and salary!=%s)",(dept[0],highestSalary1[0],highestSalary2[0],highestSalary3[0]))
			highestSalary4 = gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the fourth highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary4[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department only until topTen contains ten items, then count the remainder and append that number to topTen
			if (len(topTen)+len(hold)) <= 10:
				placeHolder = []
				for item in hold:
					placeHolder.append(list(item))
				topTen = topTen + placeHolder
				print "4a"
			else:
				count = []
				remainder = []
				for item in hold:
					while len(topTen) < 10:
						placeHolder = []
						count.append(list(item))
						placeHolder.append(list(item))
						topTen = topTen + placeHolder
				remainder = len(hold)-len(count)
				topTen.append(remainder)
				print "4b"
	#find the fifth highest salary in that department
	if (len(topTen) < 10):
		#but only if there was a fourth highest salary
		if len(highestSalary4)>0:
			cursor.execute("select max(salary) from doafull13 where dept=%s and (salary!=%s and salary!=%s and salary!=%s and salary!=%s)",(dept[0],highestSalary1[0],highestSalary2[0],highestSalary3[0],highestSalary4[0]))
			highestSalary5 = gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the fifth highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary5[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department only until topTen contains ten items, then count the remainder and append that number to topTen
			if (len(topTen)+len(hold)) <= 10:
				placeHolder = []
				for item in hold:
					placeHolder.append(list(item))
				topTen = topTen + placeHolder
				print "5a"
			else:
				count = []
				remainder = []
				for item in hold:
					while len(topTen) < 10:
						placeHolder = []
						count.append(list(item))
						placeHolder.append(list(item))
						topTen = topTen + placeHolder
				remainder = len(hold)-len(count)
				topTen.append(remainder)
				print "5b"
	#if topTen still has fewer than ten items, find the sixth highest salary in that department, but only if there was a fifth highest salary
	if (len(topTen) < 10):
		if len(highestSalary5)>0:
			cursor.execute("select max(salary) from doafull13 where dept=%s and (salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s)",(dept[0],highestSalary1[0],highestSalary2[0],highestSalary3[0],highestSalary4[0],highestSalary5[0]))
			highestSalary6 = gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the sixth highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary6[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department only until topTen contains ten items, then count the remainder and append that number to topTen
			if (len(topTen)+len(hold)) <= 10:
				placeHolder = []
				for item in hold:
					placeHolder.append(list(item))
				topTen = topTen + placeHolder
				print "6a"
			else:
				count = []
				remainder = []
				for item in hold:
					while len(topTen) < 10:
						placeHolder = []
						count.append(list(item))
						placeHolder.append(list(item))
						topTen = topTen + placeHolder
				remainder = len(hold)-len(count)
				topTen.append(remainder)
				print "6b"
	#if topTen still has fewer than ten items, find the seventh highest salary in that department, but only if there was a sixth highest salary
	if (len(topTen) < 10):
		if len(highestSalary6) > 0:
			cursor.execute("select max(salary) from doafull13 where dept=%s and (salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s)",(dept[0],highestSalary1[0],highestSalary2[0],highestSalary3[0],highestSalary4[0],highestSalary5[0],highestSalary6[0]))
			highestSalary7 = gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the seventh highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary7[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department only until topTen contains ten items, then count the remainder and append that number to topTen
			if (len(topTen)+len(hold)) <= 10:
				placeHolder = []
				for item in hold:
					placeHolder.append(list(item))
				topeTen = topTen + placeHolder
				print "7a"
			else:
				count = []
				remainder = []
				for item in hold:
					while len(topTen) < 10:
						placeHolder = []
						count.append(list(item))
						placeHolder.append(list(item))
						topTen = topTen + placeHolder
				remainder = len(hold)-len(count)
				topTen.append(remainder)
				print "7b"
	#if topTen still has fewer than ten items, find the eighth highest salary in that department, but only if there was a seventh highest salary
	if (len(topTen) < 10):
		if len(highestSalary7) > 0:
			cursor.execute("select max(salary) from doafull13 where dept=%s and (salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s)",(dept[0],highestSalary1[0],highestSalary2[0],highestSalary3[0],highestSalary4[0],highestSalary5[0],highestSalary6[0],highestSalary7[0]))
			highestSalary8 = gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the eighth highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary8[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department only until topTen contains ten items, then count the remainder and append that number to topTen
			if (len(topTen)+len(hold)) <= 10:
				placeHolder = []
				for item in hold:
					placeHolder.append(list(item))
				topTen = topTen + placeHolder
				print "8a"
			else:
				count = []
				remainder = []
				for item in hold:
					while len(topTen) < 10:
						placeHolder = []
						count.append(list(item))
						placeHolder.append(list(item))
						topTen = topTen + placeHolder
				remainder = len(hold)-len(count)
				topTen.append(remainder)
				print "8b"
	#if topTen still has fewer than ten items, find the nineth highest salary in that department, but only if there was a eighth highest salary
	if (len(topTen) < 10):
		if len(highestSalary8) > 0:
			cursor.execute("select max(salary) from doafull13 where dept=%s and (salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s)",(dept[0],highestSalary1[0],highestSalary2[0],highestSalary3[0],highestSalary4[0],highestSalary5[0],highestSalary6[0],highestSalary7[0],highestSalary8[0]))
			highestSalary9 = gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the ninth highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary9[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department only until topTen contains ten items, then count the remainder and append that number to topTen
			if (len(topTen)+len(hold)) <= 10:
				placeHolder = []
				for item in hold:
					placeHolder.append(list(item))
				topTen = topTen + placeHolder
				print "9a"
			else:
				count = []
				remainder = []
				for item in hold:
					while len(topTen) < 10:
						placeHolder = []
						count.append(list(item))
						placeHolder.append(list(item))
						topTen = topTen + placeHolder
				remainder = len(hold)-len(count)
				topTen.append(remainder)
				print "9b"
	#if topTen still has fewer than ten items, find the tenth highest salary in that department, but only if there was a ninth highest salary
	if (len(topTen) < 10):
		if len(highestSalary9) > 0:	
			cursor.execute("select max(salary) from doafull13 where dept=%s and (salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s and salary!=%s)",(dept[0],highestSalary1[0],highestSalary2[0],highestSalary3[0],highestSalary4[0],highestSalary5[0],highestSalary6[0],highestSalary7[0],highestSalary8[0],highestSalary9[0]))
			highestSalary10 = gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the ninth highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary10[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department only until topTen contains ten items, then count the remainder and append that number to topTen
			if (len(topTen)+len(hold)) <= 10:
				placeHolder = []
				for item in hold:
					placeHolder.append(list(item))
				topTen = topTen + placeHolder
				print "10a"
			else:
				count = []
				remainder = []
				for item in hold:
					while len(topTen) < 10:
						placeHolder = []
						count.append(list(item))
						placeHolder.append(list(item))
						topTen = topTen + placeHolder
				remainder = len(hold)-len(count)
				topTen.append(remainder)
				print "10b"
	print topTen
	#load data to table
	#cursor.execute("insert into generic (generic1, generic2, generic3) values(%s, %s, %s)" ,(genericList[0], genericList[1], genericList[2]))
	#clear lists for next job title analysis
#write to heshenames database
#db.commit()
print 'Success!'
cursor.close()
db.close()
