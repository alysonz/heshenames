# General query tools
import MySQLdb
import gettuple
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
dept = "you misspelled something somewhere"
firstHighestSalary = "you misspelled something somewhere"
firstHighest = []
secondHighestSalary = "you misspelled something somewhere"
secondHighest = "you misspelled something somewhere"
thirdHighestSalary = "you misspelled something somewhere"
thirdHighest = "you misspelled something somewhere"
fourthHighestSalary = "you misspelled something somewhere"
fourthHighest = "you misspelled something somewhere"
fifthHighestSalary = "you misspelled something somewhere"
fifthHighest = "you misspelled something somewhere"
sixthHighestSalary = "you misspelled something somewhere"
sixthHighest = "you misspelled something somewhere"
seventhHighestSalary = "you misspelled something somewhere"
seventhHighest = "you misspelled something somewhere"
eighthHighestSalary = "you misspelled something somewhere"
eighthHighest = "you misspelled something somewhere"
ninthHighestSalary = "you misspelled something somewhere"
ninthHighest = "you misspelled something somewhere"
tenthHighestSalary = "you misspelled something somewhere"
tenthHighest = "you misspelled something somewhere"
genericList = []
#create table to load data
#cursor.execute("create table generic (generic1 varchar(#), generic2 decimal (#,#), generic3 int(#))")
#find all distinct departments
cursor.execute("select distinct dept from doafull13")
for line in cursor:
	dept = line
	#for each distinct department, find all distinct titles
	cursor.execute("select max(salary) from doafull13 where dept=%s",(dept[0]))
	firstHighestSalary = gettuple.gettuple(cursor.fetchall())
	cursor.execute("select * from doafull13 where salary=%s and dept=%s",(firstHighestSalary[0],dept[0]))
	hold = cursor.fetchall()
	for item in hold:
		placeHolder = list(item)
		firstHighest.append(placeHolder)
	print firstHighest
	if len(firstHighest)==1:
		cursor.execute("select max(salary) from doafull13 where dept=%s and id!=%s",(dept[0],firstHighest[0][0]))
		secondHighestSalary= gettuple.gettuple(cursor.fetchall())
		cursor.execute("select * from doafull13 where salary=%s and dept=%s",(dept[0],secondHighestSalary[0]))
		hold = cursor.fetchall()
		for item in hold:
			placeHolder = list(item)
			secondHighest.append(placeHolder)
		print secondHighest
#		else:
#			secondHighest= gettuple.gettuple(hold)
#			print secondHighest 
	#cursor.execute("select id, max(salary) from doafull13 where dept=%s and id<>%s;" % (dept[0],firstHighestId[0]))
	#secondHighestId = cursor.fetchall()
	#cursor.execute("select * from doafull13 where id=%s",(secondHighestId[0]))
	#secondHighest = cursor.fetchall()
	
	
	#genericList.extend(['generic',generic[0]])
	#cursor.execute("insert into generic (generic1, generic2, generic3) values(%s, %s, %s)" ,(genericList[0], genericList[1], genericList[2]))
	firstHighest = []
	secondHighest = []	
		#clear lists for next job title analysis
#		genericList = []
#write to heshenames database
db.commit()
print 'Success!'
cursor.close()
db.close()