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
patriarchy = []
matriarchy = []
#create table to load data
cursor.execute("create table hierarchy13 (advantage varchar(1), dept varchar(40), title varchar(40), averageFemaleSalary decimal (10,5), countFemaleEmployees int(5), averageMaleSalary decimal(10,5), countMaleEmployees int(5), disparity decimal(10,5), countEmployeeGenderUnclear int(5), countNoGenderData int(5))")
#find all distinct departments
cursor.execute("select distinct dept from doagender13;")
for line in cursor:
	dept = line
	#for each distinct department, find all distinct titles
	cursor.execute("select distinct title from doagender13 where dept=%s;" , (dept[0]))
	for line in cursor:
		title = line
		#average the salary for all employees of each distinct title in each department where the chance of being female is greater than 7 in 10
		cursor.execute("select avg(salary) from doagender13 where dept=%s and title =%s and gender='F' and genderPercent > 70;", (dept[0],title[0]))
		averageFemaleSalary = cursor.fetchone()
		#count how many females have this job title in this department
		cursor.execute("select count(name) from doagender13 where dept=%s and title =%s and gender='F' and genderPercent > 70;", (dept[0],title[0]))
		countFemaleEmployees = cursor.fetchone()
		#average the salary for all employees of each distinct title in each department where the chance of being male is greater than 7 in 10
		cursor.execute("select avg(salary) from doagender13 where dept=%s and title =%s and (gender='M' or genderPercent2 > 70);" , (dept[0],title[0]))
		averageMaleSalary = cursor.fetchone()
		#count how many males have this job title in this department
		cursor.execute("select count(name) from doagender13 where dept=%s and title =%s and (gender='M' or genderPercent2 > 70);" , (dept[0],title[0    ]))
		countMaleEmployees = cursor.fetchone()
		#find employees of each distinct title in each department where gender is in question
		cursor.execute("select id from doagender13 where dept=%s and title=%s and genderPercent<70 and genderPercent>30;",(dept[0],title[0]))
		employeeGenderUnclear = cursor.fetchall()
		#count how many gender amb employees have this job title in this department
		cursor.execute("select count(name) from doagender13 where dept=%s and title=%s and genderPercent<70 and genderPercent>30;",(dept[0],title[0]))
		countEmployeeGenderUnclear = cursor.fetchone()
		#find employees of each title in each department where there is no gender data
		cursor.execute("select id from doagender13 where dept=%s and title=%s and first='none';",(dept[0],title[0]))
		noGenderData = cursor.fetchall()
		#count how many emp w/no gender info have this job title in this department
		cursor.execute("select count(name) from doagender13 where dept=%s and title=%s and first='none';",(dept[0],title[0]))
		countNoGenderData = cursor.fetchone()
		#select dept and job title when the average male salary is at least $.50 more than the average female salary
		if (averageMaleSalary[0]) and (averageFemaleSalary[0]) and (averageMaleSalary[0]-averageFemaleSalary[0] > 0):
			disparity = averageMaleSalary[0] - averageFemaleSalary[0]
			patriarchy.extend(['M',dept[0],title[0],averageFemaleSalary[0], countFemaleEmployees[0], averageMaleSalary[0], countMaleEmployees[0], disparity, countEmployeeGenderUnclear[0], countNoGenderData[0]])
			cursor.execute("insert into hierarchy13 (advantage, dept, title, averageFemaleSalary, countFemaleEmployees, averageMaleSalary, countMaleEmployees, disparity, countEmployeeGenderUnclear, countNoGenderData) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" ,(patriarchy[0], patriarchy[1], patriarchy[2], patriarchy[3], patriarchy[4], patriarchy[5], patriarchy[6], patriarchy[7], patriarchy[8], patriarchy[9]))
		elif (averageMaleSalary[0]) and (averageFemaleSalary[0]) and (averageFemaleSalary[0]-averageMaleSalary[0] > 0):
			disparity = averageFemaleSalary[0] - averageMaleSalary[0]
			matriarchy.extend(['F',dept[0],title[0],averageFemaleSalary[0], countFemaleEmployees[0], averageMaleSalary[0], countMaleEmployees[0], disparity, countEmployeeGenderUnclear[0], countNoGenderData[0]])
			cursor.execute("insert into hierarchy13 (advantage, dept, title, averageFemaleSalary, countFemaleEmployees, averageMaleSalary, countMaleEmployees, disparity, countEmployeeGenderUnclear, countNoGenderData) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" ,(matriarchy[0], matriarchy[1], matriarchy[2], matriarchy[3], matriarchy[4], matriarchy[5], matriarchy[6], matriarchy[7], matriarchy[8], matriarchy[9]))
		#clear lists for next job title analysis
		patriarchy = []
		matriarchy = []	
#write to heshenames database
db.commit()
print 'Success!'
cursor.close()
db.close()
