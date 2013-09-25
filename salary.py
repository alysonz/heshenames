# WRITE SCRIPT/QUERY TO AVERAGE MALE/FEMALE SALARY FOR EVERY DISTINCT TITLE IN EVERY AGENCY AND FLAG TITLE/AGENCY W/LARGISH MALE/FEMALE SALARY DIFFERENCE
import MySQLdb
import re
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
averageFemaleSalary = "you misspelled something somewhere"
countFemaleEmployees = "you misspelled something somewhere"
averageMaleSalary = "you misspelled something somewhere"
countMaleEmployees = "you misspelled something somewhere"
employeeGenderUnclear = []
countEmployeeGenderUnclear = "you misspelled something somewhere"
noGenderData = []
countNoGenderData = "you misspelled something somewhere"
title = "you misspelled something somewhere"
dept = "you misspelled something somewhere"
#find all distinct departments
cursor.execute("select distinct dept from doagender;")
for line in cursor:
	dept = line
	#for each distinct department, find all distinct titles
	cursor.execute("select distinct title from doagender where dept=%s;" , (dept[0]))
	for line in cursor:
		title = line
		#average the salary for all employees of each distinct title in each department where the chance of being female is greater than 7 in 10
		cursor.execute("select avg(salary) from doagender where dept=%s and title =%s and gender='F' and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))*100 > 70;", (dept[0],title[0]))
		for line in cursor:
			averageFemaleSalary = line
		#count how many females have this job title in this department
		cursor.execute("select count(name) from doagender where dept=%s and title =%s and gender='F' and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))*100 > 70;", (dept[0],title[0]))
		for line in cursor:
			countFemaleEmployees = line
		#average the salary for all employees of each distinct title in each department where the chance of being male is greater than 7 in 10
		cursor.execute("select avg(salary) from doagender where dept=%s and title =%s and (gender='M' or ((percent2*3000000)/((percent2*3000000)+(percent*3200000)))*100 > 70);" , (dept[0],title[0]))
		for line in cursor:
			averageMaleSalary = line
		#count how many males have this job title in this department
		cursor.execute("select count(name) from doagender where dept=%s and title =%s and (gender='M' or ((percent2*3000000)/((percent2*3000000)+(percent*3200000)))*100 > 70);" , (dept[0],title[0    ]))
		for line in cursor:
			countMaleEmployees = line
		#find employees of each distinct title in each department where gender is in question
		cursor.execute("select * from doagender where dept=%s and title=%s and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))<70 and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))>30;",(dept[0],title[0]))
		for line in cursor:
			line = list(line)
			for item in line:
				employeeGenderUnclear.append(item)
		#count how many gender amb employees have this job title in this department
		cursor.execute("select count(name) from doagender where dept=%s and title=%s and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))<70 and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))>30;",(dept[0],title[0]))
		for line in cursor:
			countEmployeeGenderUnclear = line
		#find employees of each title in each department where there is no gender data
		cursor.execute("select * from doagender where dept=%s and title=%s and first='none';",(dept[0],title[0]))
		for line in cursor:
			line = list(line)
			for item in line:	
				noGenderData.append(item)
		#count how many emp w/no gender info have this job title in this department
		cursor.execute("select count(name) from doagender where dept=%s and title=%s and first='none';",(dept[0],title[0]))
		for line in cursor:
			countNoGenderData = line
		#select dept and job title when the average male salary is at least $.50 more than the average female salary
		if (averageMaleSalary[0]) and (averageFemaleSalary[0]) and (averageMaleSalary[0]-averageFemaleSalary[0] > .5):
			print "FLAG!!! THE PATRIARCHY LIVES HERE!"
			#return offending department and job title with average female salary and average male salary
			print "%s, %s" %(dept[0],title[0])
			print "Female Salary  %s, Number employed %s" %(averageFemaleSalary, countFemaleEmployees)
			print "Male Salary  %s, Number employed %s" %(averageMaleSalary, countMaleEmployees)
			#if there are any employees in that department with that job title with gender ambiguous names, return the number of such employees and their employee data
			if countEmployeeGenderUnclear>0:
				print "Gender unlear for %s employees:" % (countEmployeeGenderUnclear)
				print employeeGenderUnclear
			#if there are any employees in that department with that job title with no gender data, return the number of such employees and their employee data
			if countNoGenderData>0:
				print "No gender data for %s employees:" % (countNoGenderData)
				print noGenderData
		#repeat all for department and job titles when the average female salary is at least %.50 more than the average male salary
		if (averageMaleSalary[0]) and (averageFemaleSalary[0]) and (averageFemaleSalary[0]-averageMaleSalary[0] > .5):
			print "FLAG!!! THE MATRIARCHY LIVES HERE!"
			print "%s, %s" %(dept[0],title[0])
			print "Male Salary  %s, Number employed %s" %(averageMaleSalary, countMaleEmployees)
			print "Female Salary  %s, Number employed %s" %(averageFemaleSalary, countFemaleEmployees)
			if countEmployeeGenderUnclear>0:
				print "Gender unlear for %s employees:" % (countEmployeeGenderUnclear)
				print employeeGenderUnclear
			if countNoGenderData>0:
				print "No gender data for %s employees:" % (countNoGenderData)
				print noGenderData
		#clear lists for next job title analysis
		employeeGenderUnclear = []
		noGenderData = []	
#create table to load list data information	
#cursor.execute("create table final (id int(10), dept varchar(40), name varchar(40), title varchar(40), salary decimal (10,5), first varchar(10), gender varchar(2), percent decimal(10,5), percentile decimal(10,5), rank int(10), first2 varchar(10), gender2 varchar(2), percent2 decimal(10,5), percentile2 decimal(10,5), rank2 int(10))")
#normalize lists within data to contain placeholders for every column in query6 table
	#for each list within data, insert each item into each column in query6 table
	#cursor.execute("insert into final (id, dept, name, title, salary, first, gender, percent, percentile, rank, first2, gender2, percent2, percentile2, rank2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" ,(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14]))
#write to heshenames database
#db.commit()
print 'Success!'
cursor.close()
db.close()
