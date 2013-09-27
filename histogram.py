# WRITE SCRIPT/QUERY TO AVERAGE MALE/FEMALE SALARY FOR EVERY DISTINCT TITLE IN EVERY AGENCY AND FLAG TITLE/AGENCY W/LARGISH MALE/FEMALE SALARY DIFFERENCE
import MySQLdb
import re
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
dept = "you misspelled something somewhere"
deptMaleDisparity = []
deptFemaleDisparity = []
#create table to load data
cursor.execute("create table histogram (dept varchar(40), advantage varchar(1), disparity decimal(10,5))")
cursor.execute("select distinct dept from hierarchy")
for line in cursor:
	dept = line
	cursor.execute("select sum(disparity) from hierarchy where dept = %s and advantage = 'M'",(dept[0]))
	for line in cursor:
		deptMaleDisparity.extend([dept[0],'M',line[0]])
	cursor.execute("select sum(disparity) from hierarchy where dept = %s and advantage = 'F'",(dept[0]))
	for line in cursor:
		deptFemaleDisparity.extend([dept[0],'F', line[0]])
	cursor.execute("insert into histogram (dept, advantage, disparity) values (%s, %s, %s)", (deptMaleDisparity[0], deptMaleDisparity[1], deptMaleDisparity[2]))
	cursor.execute("insert into histogram (dept, advantage, disparity) values (%s, %s, %s)", (deptFemaleDisparity[0], deptFemaleDisparity[1], deptFemaleDisparity[2]))
	#clear lists for next job title analysis
	deptMaleDisparity = []
	deptFemaleDisparity = []	
#write to heshenames database
db.commit()
print 'Success!'
cursor.close()
db.close()
