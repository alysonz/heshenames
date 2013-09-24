# WRITE SCRIPT/QUERY TO AVERAGE MALE/FEMALE SALARY FOR EVERY DISTINCT TITLE IN EVERY AGENCY AND FLAG TITLE/AGENCY W/LARGISH MALE/FEMALE SALARY DIFFERENCE
import MySQLdb
import re
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
af = []
am = []
ab = 1
no = 1
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
		#HAVE ACCOUNTED FOR NAMES WHERE ONLY MALE DATA APPLIES
		cursor.execute("select avg(salary) from doagender where dept=%s and title =%s and gender='F' and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))*100 > 70;", (dept[0],title[0]))
		for b in cursor:
			af=list(b)
			print dept
			print 'avg fem salary for ' + title[0]
			print af
		#count how many females have this job title in this department

		#average the salary for all employees of each distinct title in each department where the chance of being male is greater than 7 in 10
		#HAVE NOT ACCOUNTED FOR NAMES WHERE ONLY MALE DATA APPLIES
		cursor.execute("select avg(salary) from doagender where dept=%s and title =%s and ((percent2*3000000)/((percent2*3000000)+(percent*3200000)))*100 > 70 or gender='M';" , (dept[0],title[0]))
		for c in cursor:
			am = list(c)
			print 'avg male salary for ' + title[0]
			print am
		#count how many males have this job title in this department

		#find employees of each distinct title in each department where gender is in question
		cursor.execute("select * from doagender where dept=%s and title=%s and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))<70 and ((percent*3200000)/((percent2*3000000)+(percent*3200000)))>30;",(dept[0],title[0]))
		for line in cursor:
			ab = line
			print 'ambig gender for %s',(title[0])
			print ab
		#count how many gender amb employees have this job title in this department

		#find employees of each title in each department where there is no gender data
		cursor.execute("select * from doagender where dept=%s and title=%s and first='none';",(dept[0],title[0]))
		for line in cursor:
			no = list(line)
			print 'no gender data for emp'
			print no
		#count how many emp w/no gender info have this job title in this department
		

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
