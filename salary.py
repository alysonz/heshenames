# WRITE SCRIPT/QUERY TO AVERAGE MALE/FEMALE SALARY FOR EVERY DISTINCT TITLE IN EVERY AGENCY AND FLAG TITLE/AGENCY W/LARGISH MALE/FEMALE SALARY DIFFERENCE
import MySQLdb
import re
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
af = []
am = []
ab = []
no = []
title = 1
dept = 1
#find all distinct departments
cursor.execute("select distinct dept from doagender;")
for line in cursor:
	dept = list(line)
	#for each distinct department, find all distinct titles
	cursor.execute("select distinct title from doagender where dept=%s;" , (dept[0]))
	for a in cursor:
		title = list(a)
		#average the salary for all employees of each distinct title in each department where the chance of being female is greater than 7 in 10
		cursor.execute("select avg(salary) from doagender where dept=%s and title =%s and gender='F' and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))*100 > 70;", (dept[0],title[0]))
		for b in cursor:
			averageFemaleSalary=list(b)
			print dept
			print 'avg fem salary for ' + title[0]
			print averageFemaleSalary
		#count how many females have this job title in this department
		cursor.execute("select count(name) from doagender where dept=%s and title =%s and gender='F' and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))*100 > 70;", (dept[0],title[0]))
		for d in cursor:
			print d
		#average the salary for all employees of each distinct title in each department where the chance of being male is greater than 7 in 10
		cursor.execute("select avg(salary) from doagender where dept=%s and title =%s and (gender='M' or ((percent2*3000000)/((percent2*3000000)+(percent*3200000)))*100 > 70);" , (dept[0],title[0]))
		for c in cursor:
			averageMaleSalary = list(c)
			print 'avg male salary for ' + title[0]
			print averageMaleSalary
		#count how many males have this job title in this department
		cursor.execute("select count(name) from doagender where dept=%s and title =%s and (gender='M' or ((percent2*3000000)/((percent2*3000000)+(percent*3200000)))*100 > 70);" , (dept[0],title[0    ]))
		for e in cursor:
			print e
		#find employees of each distinct title in each department where gender is in question
		cursor.execute("select * from doagender where dept=%s and title=%s and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))<70 and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))>30;",(dept[0],title[0]))
		for f in cursor:
			employeeGenderUnclear = list(f)
			print 'ambig gender for %s',(title[0])
			print employeeGenderUnclear
		#count how many gender amb employees have this job title in this department
		cursor.execute("select count(name) from doagender where dept=%s and title=%s and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))<70 and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))>30;",(dept[0],title[0]))
		for g in cursor:
			print g
		#find employees of each title in each department where there is no gender data
		cursor.execute("select * from doagender where dept=%s and title=%s and first='none';",(dept[0],title[0]))
		for line in cursor:
			noGenderData = list(line)
			print 'no gender data for emp'
			print noGenderData
		#count how many emp w/no gender info have this job title in this department
		cursor.execute("select count(name) from doagender where dept=%s and title=%s and first='none';",(dept[0],title[0]))
		for h in cursor:
			print h
		#select dept and job title when the average male salary is at least $.50 more than the average female salary
		if (averageMaleSalary!=None) and (averageFemaleSalary!=None):
			if (float(averageMaleSalary[0])-float(averageFemaleSalary[0]) > .5):
				print dept[0]+title[0] + " FLAG!!! THE PATRIARCHY LIVES HERE!"
		#select dept and job title when the average female salary is at least $.50 more than the average male salary
	#	cursor.execute("select %s, %s where %i-%i>.5;",(dept[0],title[0],query1,query2))
	#	for j in cursor:
	#		print list(j) + " FLAG!!! THE MATRIARCHY LIVES HERE!"
#create table to load list data information	
#cursor.execute("create table final (id int(10), dept varchar(40), name varchar(40), title varchar(40), salary decimal (10,5), first varchar(10), gender varchar(2), percent decimal(10,5), percentile decimal(10,5), rank int(10), first2 varchar(10), gender2 varchar(2), percent2 decimal(10,5), percentile2 decimal(10,5), rank2 int(10))")
#normalize lists within data to contain placeholders for every column in query6 table
	#for each list within data, insert each item into each column in query6 table
	#cursor.execute("insert into final (id, dept, name, title, salary, first, gender, percent, percentile, rank, first2, gender2, percent2, percentile2, rank2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" ,(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14]))
#write to heshenames database
#cnx.commit()
print af
print 'Success!'
cursor.close()
cnx.close()
