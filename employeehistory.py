#General query tools
import MySQLdb
import re
import gettuple
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
#set up variables
departmentAndTitle = "you misspelled something somewhere"
doaGender13 = "you misspelled something somewhere"
employmentHistory2012 = "you misspelled something somewhere"
employmentIndex2012 = [2012]
employmentHistory2011 = "you misspelled something somewhere"
employmentIndex2011 = [2011]
employmentHistory2010 = "you misspelled something somewhere"
employmentIndex2010 = [2010]
employmentHistory2009 = "you misspelled something somewhere"
employmentIndex2009 = [2009]
#create table to load data
#cursor.execute("create table generic (generic1 varchar(#), generic2 decimal (#,#), generic3 int(#))")
#search for disparity flags in specific departments, return deparment and job title
#select department and title of cases flagged for genderized wage disparity
cursor.execute("select dept, title from hierarchy13 where disparity>0 and dept like '%real estate%'")
#for each flagged title in the department, select all employees with that job title in that department
for line in cursor:
	departmentAndTitle = line
	print departmentAndTitle
	cursor.execute("select * from doagender13 where dept=%s and title=%s;" , (departmentAndTitle[0],departmentAndTitle[1]))
	#for each employee in the flagged department and job title, find all existing employment history with the state from 2012, 2011, 2010 and 2009
	for line in cursor:
		doaGender13 = list(line)
		cursor.execute("select * from doafull12 where name like %s",(doaGender13[2]))
		employmentHistory2012 = gettuple.gettuple(cursor.fetchall())
		#if employee has employment data from 2012, check if they worked in the same dept with the same title with a salary that was the same, more or less than 2013. Store results in list.
		if len(employmentHistory2012)>0:
			if (employmentHistory2012[1]==departmentAndTitle[0]):
				employmentIndex2012.append("Dept-Yes")
			else:
				employmentIndex2012.append("Dept-No")
			if (employmentHistory2012[3]==departmentAndTitle[1]):
				employmentIndex2012.append("Title-Yes")
			else:
				employmentIndex2012.append("Title-No")
			if (doaGender13[4]==employmentHistory2012[4]):
				employmentIndex2012.append("Salary-Same")
			elif (doaGender13[4]>employmentHistory2012[4]):
				employmentIndex2012.append("Salary-Less")
			elif (doaGender13[4]<employmentHistory2012[4]):
				employmentIndex2012.append("Salary-More")
			doaGender13 = doaGender13 + employmentIndex2012
		else:
			doaGender13.extend([2012,None,None,None])
		cursor.execute("select * from doafull11 where name like %s",(doaGender13[2]))
		employmentHistory2011 = gettuple.gettuple(cursor.fetchall())
		#if employee has employment data from 2011, check if they worked in the same dept with the same title with a salary that was the same, more or less than 2013. Store results in list.
		if len(employmentHistory2011)>0:
			if (employmentHistory2011[1]==departmentAndTitle[0]):
				employmentIndex2011.append("Dept-Yes")
			else:
				employmentIndex2011.append("Dept-No")
			if (employmentHistory2011[3]==departmentAndTitle[1]):
				employmentIndex2011.append("Title-Yes")
			else:
				employmentIndex2011.append("Title-No")
			if (doaGender13[4]==employmentHistory2011[4]):
				sameSalary2011 = "Salary-Yes"
				employmentIndex2011.append("Salary-Same")
			elif (doaGender13[4]>employmentHistory2011[4]):
				employmentIndex2011.append("Salary-Less")
			elif (doaGender13[4]<employmentHistory2011[4]):
				employmentIndex2011.append("Salary-More")
			doaGender13 = doaGender13 + employmentIndex2011
		else:
			doaGender13.extend([2011,None,None,None])
		cursor.execute("select * from doafull10 where name like %s",(doaGender13[2]))
		employmentHistory2010 = gettuple.gettuple(cursor.fetchall())
		#if employee has employment data from 2010, check if they worked in the same dept with the same title with a salary that was the same, more or less than 2013. Store results in list.
		if len(employmentHistory2010)>0:
			if (employmentHistory2010[1]==departmentAndTitle[0]):
				employmentIndex2010.append("Dept-Yes")
			else:
				employmentIndex2010.append("Dept-No")
			if (employmentHistory2010[3]==departmentAndTitle[1]):
				employmentIndex2010.append("Title-Yes")
			else:
				employmentIndex2010.append("Title-No")
			if (doaGender13[4]==employmentHistory2010[4]):
				employmentIndex2010.append("Salary-Same")
			elif (doaGender13[4]>employmentHistory2010[4]):
				employmentIndex2010.append("Salary-Less")
			elif (doaGender13[4]<employmentHistory2010[4]):
				employmentIndex2010.append("Salary-More")
			doaGender13 = doaGender13 + employmentIndex2010
		else:
			doaGender13.extend([2010,None,None,None])
		cursor.execute("select * from doafull09 where name like %s",(doaGender13[2]))
		employmentHistory2009 = gettuple.gettuple(cursor.fetchall())
		#if employee has employment data from 2009, check if they worked in the same dept with the same title with a salary that was the same, more or less than 2013. Store results in list.
		if len(employmentHistory2009)>0:
			if (employmentHistory2009[1]==departmentAndTitle[0]):
				employmentIndex2009.append("Dept-Yes")
			else:
				employmentIndex2009.append("Dept-No")
			if (employmentHistory2009[3]==departmentAndTitle[1]):
				employmentIndex2009.append("Title-Yes")
			else:
				employmentIndex2009.append("Title-No")
			if (doaGender13[4]==employmentHistory2009[4]):
				employmentIndex2009.append("Salary-Same")
			elif (doaGender13[4]>employmentHistory2009[4]):
				employmentIndex2009.append("Salary-Less")
			elif (doaGender13[4]<employmentHistory2009[4]):
				employmentIndex2009.append("Salary-More")
			doaGender13 = doaGender13 + employmentIndex2009
		else:
			doaGender13.extend([2009,None,None,None])
		print doaGender13
		#reset employment history index lists for analysis of next employee
		employmentIndex2012 = [2012]
		employmentIndex2011 = [2011]
		employmentIndex2010 = [2010]
		employmentIndex2009 = [2009]
	#cursor.execute("insert into generic (generic1, generic2, generic3) values(%s, %s, %s)" ,(genericList[0], genericList[1], genericList[2]))
#write to heshenames database
#db.commit()
print 'Success!'
cursor.close()
db.close()
