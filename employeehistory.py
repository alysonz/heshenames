#General query tools
import MySQLdb
import re
import gettuple
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
#set up variables
departmentTitleAdvantage = "you misspelled something somewhere"
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
cursor.execute("create table disparityGT1(id int(10), advantage varchar(1), disparity decimal(10,5), dept varchar(40), name varchar (40), title varchar(40), salary decimal(10,5), first varchar(20), genderPercent decimal(10,5), gender varchar(1), percent decimal(10,5), percentile decimal(10,5), rank int(10), first2 varchar(20), genderPercent2 decimal(10,5), gender2 varchar(1), percent2 decimal(10,5), percentile2 decimal(10,5), rank2 int(10), year12 int(4), dept12 varchar(10), title12 varchar(10), salary12 varchar(15), year11 int(4), dept11 varchar(10), title11 varchar(10), salary11 varchar(15), year10 int(4), dept10 varchar(10), title10 varchar(10), salary10 varchar(15), year09 int(4), dept09 varchar(10), title09 varchar(10), salary09 varchar(15))")
#search for disparity flags in specific departments, return deparment and job title
#select department and title of cases flagged for genderized wage disparity
cursor.execute("select dept, title, advantage, disparity from hierarchy13 where disparity>1")
#for each flagged title in the department, select all employees with that job title in that department
for line in cursor:
	departmentTitleAdvantage = line
	print departmentTitleAdvantage
	cursor.execute("select * from doagender13 where dept=%s and title=%s;" , (departmentTitleAdvantage[0],departmentTitleAdvantage[1]))
	#for each employee in the flagged department and job title, find all existing employment history with the state from 2012, 2011, 2010 and 2009
	for line in cursor:
		doaGender13 = list(line)
		cursor.execute("select * from doafull12 where name=%s",(doaGender13[2]))
		employmentHistory2012 = gettuple.gettuple(cursor.fetchall())
		#if employee has employment data from 2012, check if they worked in the same dept with the same title with a salary that was the same, more or less than 2013. Store results in list.
		if len(employmentHistory2012)>0:
			if (employmentHistory2012[1]==departmentTitleAdvantage[0]):
				employmentIndex2012.append("Dept-Yes")
			else:
				employmentIndex2012.append("Dept-No")
			if (employmentHistory2012[3]==departmentTitleAdvantage[1]):
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
		cursor.execute("select * from doafull11 where name=%s",(doaGender13[2]))
		employmentHistory2011 = gettuple.gettuple(cursor.fetchall())
		#if employee has employment data from 2011, check if they worked in the same dept with the same title with a salary that was the same, more or less than 2013. Store results in list.
		if len(employmentHistory2011)>0:
			if (employmentHistory2011[1]==departmentTitleAdvantage[0]):
				employmentIndex2011.append("Dept-Yes")
			else:
				employmentIndex2011.append("Dept-No")
			if (employmentHistory2011[3]==departmentTitleAdvantage[1]):
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
		cursor.execute("select * from doafull10 where name=%s",(doaGender13[2]))
		employmentHistory2010 = gettuple.gettuple(cursor.fetchall())
		#if employee has employment data from 2010, check if they worked in the same dept with the same title with a salary that was the same, more or less than 2013. Store results in list.
		if len(employmentHistory2010)>0:
			if (employmentHistory2010[1]==departmentTitleAdvantage[0]):
				employmentIndex2010.append("Dept-Yes")
			else:
				employmentIndex2010.append("Dept-No")
			if (employmentHistory2010[3]==departmentTitleAdvantage[1]):
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
		cursor.execute("select * from doafull09 where name=%s",(doaGender13[2]))
		employmentHistory2009 = gettuple.gettuple(cursor.fetchall())
		#if employee has employment data from 2009, check if they worked in the same dept with the same title with a salary that was the same, more or less than 2013. Store results in list.
		if len(employmentHistory2009)>0:
			if (employmentHistory2009[1]==departmentTitleAdvantage[0]):
				employmentIndex2009.append("Dept-Yes")
			else:
				employmentIndex2009.append("Dept-No")
			if (employmentHistory2009[3]==departmentTitleAdvantage[1]):
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
		#reset employment history index lists for analysis of next employee
		employmentIndex2012 = [2012]
		employmentIndex2011 = [2011]
		employmentIndex2010 = [2010]
		employmentIndex2009 = [2009]
		cursor.execute("insert into disparityGT1 (id, advantage, disparity, dept, name, title, salary, first, genderPercent, gender, percent, percentile, rank, first2, genderPercent2, gender2, percent2, percentile2, rank2, year12, dept12, title12, salary12, year11, dept11, title11, salary11, year10, dept10, title10, salary10, year09, dept09, title09, salary09) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" ,(doaGender13[0], departmentTitleAdvantage[2], departmentTitleAdvantage[3], doaGender13[1], doaGender13[2], doaGender13[3], doaGender13[4], doaGender13[5], doaGender13[6], doaGender13[7], doaGender13[8], doaGender13[9], doaGender13[10], doaGender13[11], doaGender13[12], doaGender13[13], doaGender13[14], doaGender13[15], doaGender13[16], doaGender13[17], doaGender13[18], doaGender13[19], doaGender13[20], doaGender13[21], doaGender13[22], doaGender13[23], doaGender13[24], doaGender13[25], doaGender13[26], doaGender13[27], doaGender13[28], doaGender13[29], doaGender13[30], doaGender13[31], doaGender13[32]))
#write to heshenames database
db.commit()
print 'Success!'
cursor.close()
db.close()
