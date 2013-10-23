# General query tools
import MySQLdb
import gettuple
import re
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
dept = "you misspelled something somewhere"
highestSalary = "you misspelled something somewhere"
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
	highestSalary = gettuple.gettuple(cursor.fetchall())
	#find the employee/s with the highest salary in that department
	cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary[0],dept[0]))
	hold = cursor.fetchall()
	#add that/those employee/s to the topTen list for that department
	for item in hold:
		placeHolder = list(item)
		topTen.append(placeHolder)
	#if there was only one employee with the top salary in that department
	if len(topTen)==1:
		for line in topTen:
			#find the next highest salary in that department
			cursor.execute("select max(salary) from doafull13 where dept=%s and id!=%s",(dept[0],line[0]))
			highestSalary=gettuple.gettuple(cursor.fetchall())
			#find the employee/s with the next highest salary in that department
			cursor.execute("select * from doafull13 where salary=%s and dept=%s",(highestSalary[0], dept[0]))
			hold = cursor.fetchall()
			#add that/those employee/s to the topTen list for that department
			for item in hold:
				placeHolder = []
				placeHolder.append(list(item))
				topTen = topTen + placeHolder
	#while there are fewer than ten employees in the topTen list for that department
	while (len(topTen)>1) and (len(topTen)<11):
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
