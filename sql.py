import mysql.connector
import re
cnx = mysql.connector.connect(user='alyson', password='thetempleofwhollyness', host='localhost', database='heshenames')
cursor = cnx.cursor()
d = 1
n = 1
f = 1
k = 1
data = []
heshenames = open('heshenames.txt', 'w')
while d < 10:
#first take id from doanames 1-10
	query3 = ("select name from doanames where id=%s;" %(d))
	cursor.execute(query3)
	for this in cursor:
		n = this
	query4 = ("select * from heshe where name='%s';" %(n))
	cursor.execute(query4)
	for that in cursor:
		print that
		f = that
		print "taco"
		print f
	query5 = ("select * from doafull where id=%s;" %(d))
	cursor.execute(query5)
	for other in cursor:
		k = other
	data.append(k + f)
	d=d+1
print data
#a = []
#b = []
#query7 = 1
#for line in data:
#	a.append(list(line))
#query6 = ("create table final (id int(10), dept varchar(40), fullname varchar(40), title varchar(40), salary int(10), first varchar(10), gender varchar(2), percent decimal(10,5), percentile decimal(10,5), rank int(10), first2 varchar(10), gender2 varchar(2), percent2 decimal(10,5), percentile2 decimal(10,5), rank2 int(10));")
#cursor.execute(query6)
#for line in a:
#	query7 = ("insert into final (id, dept, fullname, title, salary, first, gender, percent, percentile, rank, first2, gender2, percent2, percentile2, rank2) values (%s);" % (line))
cursor.close()
cnx.close()
