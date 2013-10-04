#General query tools
import MySQLdb
import re
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
departmentTitle = "you misspelled something somewhere"
doaGender13 = "you misspelled something somewhere"
employmentHistory2012 = "you misspelled something somewhere"
employmentHistory2011 = "you misspelled something somewhere"
employmentHistory2010 = "you misspelled something somewhere"
employmentHistory2009 = "you misspelled something somewhere"
genericList = []
#create table to load data
#cursor.execute("create table generic (generic1 varchar(#), generic2 decimal (#,#), generic3 int(#))")
#search for disparity flags in specific departments, return deparment and job title
cursor.execute("select dept, title from hierarchy13 where disparity>0 and dept like '%real estate%'")
for line in cursor:
	departmentTitle = line
	#select employment information for each employee contained in the flagged department and job title
	cursor.execute("select * from doagender13 where dept=%s and title=%s;" , (departmentTitle[0],departmentTitle[1]))
	#for each employee in the flagged department and job title, find all existing employment history from 2012, 2011, 2010 and 2009
	for line in cursor:
		doaGender13 = line
		print doaGender13
		cursor.execute("select * from doafull12 where name like %s",(doaGender13[2]))
	#	employmentHistory2012 = cursor.fetchall()
		print len(cursor.fetchall())
		print cursor.fetchall()
		#if len(employmentHistory2012)>1:
		#	if (employmentHistory2012[1]==departmentTitle[0]):
				#sameDepartment2012 = True
				#print sameDepartment2012
		#if (employmentHistory2012[2]):
			#if (employmentHistory2012[2]==departmentTitle[1]):
			#	sameTitle2012 = True
			#	print sameTitle2012
		cursor.execute("select * from doafull11 where name like %s",(doaGender13[2]))
		employmentHistory2011 = cursor.fetchall()
		if (employmentHistory2011):
			print "2011 %s" % (employmentHistory2011)
		cursor.execute("select * from doafull10 where name like %s",(doaGender13[2]))
		employmentHistory2010 = cursor.fetchall()
		if (employmentHistory2010):
			print "2010 %s" % (employmentHistory2010)
		cursor.execute("select * from doafull09 where name like %s",(doaGender13[2]))
		employmentHistory2009 = cursor.fetchall()
		if (employmentHistory2009):
			print "2009 %s" % (employmentHistory2009)
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
