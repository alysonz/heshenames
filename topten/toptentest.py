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
iterate = 1
topTen = []
hold = "you misspelled something somewhere"
placeHolder = "you misspelled something somewhere"
baseQuery = '"select max(salary) from doafull13 where dept=%s and id!=%s'
#create table to load data
#cursor.execute("create table generic (generic1 varchar(#), generic2 decimal (#,#), generic3 int(#))")
#find all distinct departments
cursor.execute("select distinct dept from doafull13")
for line in cursor:
	dept = line
	#for each distinct department, find the highest salary in that department
	cursor.execute("select max(salary) from doafull13 where dept=%s",(dept[0]))
	highestSalary1 = gettuple.gettuple(cursor.fetchall())
	#find the employee/s with the highest salary in that department
	cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary1[0],dept[0]))
	hold = cursor.fetchall()
	#add that/those employee/s to the topTen list for that department
	for item in hold:
		placeHolder = list(item)
		topTen.append(placeHolder)
	#if there was only one employee with the top salary in that department
	if len(topTen)==1:
		for line in topTen:
			#find the second highest salary in that department
			cursor.execute("select max(salary) from doafull13 where dept=%s and id!=%s",(dept[0],line[0]))
			highestSalary2 = gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the next highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary2[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department
			for item in hold:
				placeHolder = []
				placeHolder.append(list(item))
				topTen = topTen + placeHolder
	#if there are fewer than ten employees in the topTen list for that department
	if (len(topTen)<11):
		#find the third highest salary in that department
		cursor.execute("select max(salary) from doafull13 where dept=%s and salary!=%s or salary!=%s",(dept[0],highestSalary1[0],highestSalary2[0])
		highestSalary3 = gettuple.gettuple(cursor.fetchall())
		#find the employee/s with the third highest salary in that department, but only if there was a third highest salary
		if len(highestSalary3)>0:
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary3[0], dept[0])
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department
			for item in hold:
				placeHolder = []
				placeHolder.append(list(item))
				topTen = topTen + placeHolder
	#if there are still fewer than ten employees in the topTen list for that department, find the fourth highest salary in that department
	if (len(topTen)<11):
		#but only if there was a third highest salary
		if len(highestSalary3)>0:
			cursor.execute("select max(salary) from doafull13 where dept=%s and salary!=%s or salary!=%s or salary!=%s",(dept[0],highestSalary1[0],highestSalary2[0],highestSalary3[0])
			highestSalary4 = gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the fourth highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary4[0], dept[0])
			hold = cursor.fetchall()
			#conditionally add that/those employee/s to the topTen list for that department

#WAIT, DOES THIS MEAN THAT FOR EVERY EMPLOYEE IN HOLD I AM APPENDING THAT EMPLOYEE, ADDING THAT LIST TO TOPTEN, AND THEN DOING IT AGAIN? SO TOPTEN PLUS EMPLOYEE 1, TOPTEN PLUS EMPLOYEE 1 AND 2.... ETC?

#WRITE A CONDITION THAT SAYS, IF ADDING EMPLOYEES WILL CAUSE TOPTEN TO EXCEED 10 ITEMS, THEN ADD UP UNTIL 10 ITEMS AND THEN COUNT HOW MANY ARE LEFT AND APPEND THAT AS THE LAST ITEM TO SHOW HOW MANY EMPLOYEES SHARE THAT SALARY
			for item in hold:
				placeHolder = []
				placeHolder.append(list(item)) 
				topTen = topTen + placeHolder

	#find the fifth highest salary in that department
	if (len(topTen)<11):
		#but only if there was a fourth highest salary
		if len(highestSalary4)>0:
			cursor.execute("select max(salary) from doafull13 where dept=%s and salary!=%s or salary!=%s or salary!=%s or salary!=%s",(dept[0],highestSalary1[0],highestSalary2[0],highestSalary3[0],highestSalary4[0])
			highestSalary5 = gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the fifth highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary5[0], dept[0])
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department
			for item in hold:
				placeHolder = []
				placeHolder.append(list(item))
				topTen = topTen + placeHolder
			




#EVERYTHING AFTER HERE IS JUNK

		#build a query for that department that deselects for the employees already obtained by eliminating their id numbers from the searchable pool (why did I do that by id and not salary?) 
		while iterate<len(topTen):
			baseQuery = baseQuery + " or id!=%s"
			iterate = iterate + 1
		baseQuery = baseQuery + '",(dept[0],'
		iterate = 0	
		#by selecting the ids from topTen (which is a list of lists)
		while iterate<(len(topTen)-1):
			baseQuery = baseQuery + "topTen[%s][0],"%(iterate)
			iterate = iterate + 1
		baseQuery = baseQuery + "topTen[%s][0])"%(iterate)
		#execute the tailored query to find the next highest salary in that department
		cursor.execute(baseQuery)
		highestSalary = gettuple.gettuple(cursor.fetchall())
		#find the employee/s with the next hightest salary in that department
		cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary[0],dept[0]))
		hold = cursor.fetchall()
		#add that/those employee/s to the topTen list for that department
		for item in hold:
			placeHolder = []
			placeHolder.append(list(item))
			topTen = topTen + placeHolder
		#reset query for looping until topTen contains at least the top ten highest paid employees in that department
		baseQuery = '"select max(salary) from doafull13 where dept=%s and id!=%s'

#EVERTHING BEFORE HERE IS JUNK
	
	print topTen			
	#load data to table
	#cursor.execute("insert into generic (generic1, generic2, generic3) values(%s, %s, %s)" ,(genericList[0], genericList[1], genericList[2]))
	#clear lists for next job title analysis
	topTen = []
#write to heshenames database
#db.commit()
print 'Success!'
cursor.close()
db.close()
