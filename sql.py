import mysql.connector
import re
cnx = mysql.connector.connect(user='alyson', password='thetempleofwhollyness', host='localhost', database='heshenames')
cursor = cnx.cursor()
#set up variables. d as iterable id. n as doa name in query3 result. f as gender result list. c and k as list results. data as concatinated c and k.
d = 1
n = 1
f = []
c = []
k = 1
data = []
#set end condition for d. start loop through all doanames
while d < 38635:
#first take id from doanames 1-38634
	cursor.execute("select name from doanames13 where id=%s" %(d))
	for this in cursor:
		#store doaname in n
		n = this
	#select every row in name gender database where name matches doaname
	cursor.execute("select * from heshe where name=%s" ,(n))
	#store potentially multiple results in f, convert tuple to list
	for that in cursor:
		that = list(that)
		f.append(that)
		f=list(f)
	#restore lists in list f as items in list c.
	for line in f:
		for stuff in line:
			c.append(stuff)
	#select row in employee information database where id matches the id of employee name in this iteration
	cursor.execute("select * from doafull13 where id=%d" %(d))
	#store employee info in k, convert tuple to list
	for other in cursor:
		k = other
		k=list(k)
	#concatinate list of employee information with list of name gender information
	data.append(k + c)
	#iterate to next name id
	d=d+1
	#clear f and c so that lists don't stack information
	f=[]
	c=[]
#establish query7 outside of for loop	
query7 = 1
#create table to load list data information	
cursor.execute("create table final13 (id int(10), dept varchar(40), name varchar(40), title varchar(40), salary decimal (10,5), first varchar(10), gender varchar(2), percent decimal(10,5), percentile decimal(10,5), rank int(10), first2 varchar(10), gender2 varchar(2), percent2 decimal(10,5), percentile2 decimal(10,5), rank2 int(10))")
#normalize lists within data to contain placeholders for every column in query6 table
for line in data:
	if len(line) < 15:
		line.extend(['none', 'none', '0.0', '0.0', '0'])
	if len(line) < 15:
		line.extend(['none', 'none', '0.0', '0.0', '0'])
	if len(line) <> 15:
		print line
	#for each list within data, insert each item into each column in query6 table
	cursor.execute("insert into final13 (id, dept, name, title, salary, first, gender, percent, percentile, rank, first2, gender2, percent2, percentile2, rank2) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" ,(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14]))
#write to heshenames database
cnx.commit()
print 'Success!'
cursor.close()
cnx.close()
