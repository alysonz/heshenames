# General query tools
import MySQLdb
import re
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
departmentTitle = "you misspelled something somewhere"
doaGender13 = "you misspelled something somewhere"
employmentHistory = "you misspelled something somewhere"
genericList = []
#create table to load data
#cursor.execute("create table generic (generic1 varchar(#), generic2 decimal (#,#), generic3 int(#))")
#find all distinct departments
cursor.execute("select dept, title from hierarchy13 where disparity>0 and dept like '%real estate%'")
for line in cursor:
	departmentTitle = line
	#for each distinct department, find all distinct titles
	cursor.execute("select * from doagender13 where dept=%s and title=%s;" , (departmentTitle[0],departmentTitle[1]))
	for line in cursor:
		doaGender13 = line
		cursor.execute("select * from doafull12, doafull11, doafull10, doafull09 where doafull12.name like %s and doafull11.name like %s and doafull10.name like %s and doafull09.name like %s",(doaGender13[2],doaGender13[2],doaGender13[2],doaGender13[2]))
		employmentHistory = cursor.fetchall()
		print doaGender13 + employmentHistory
	#generic = cursor.fetchall()
	#genericList.extend(['generic',generic[0]])
	#cursor.execute("insert into generic (generic1, generic2, generic3) values(%s, %s, %s)" ,(genericList[0], genericList[1], genericList[2]))
		#clear lists for next job title analysis
	#	genericList = []
#write to heshenames database
#db.commit()
print 'Success!'
cursor.close()
db.close()
