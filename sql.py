import mysql.connector
import re
cnx = mysql.connector.connect(user='alyson', password='thetempleofwhollyness', host='localhost', database='heshenames')
cursor = cnx.cursor()
d = 1
n = 1
f = []
c = []
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
		that = list(that)
		f.append(that)
		f=list(f)
	for line in f:
		for stuff in line:
			c.append(stuff)
	query5 = ("select * from doafull where id=%s;" %(d))
	cursor.execute(query5)
	for other in cursor:
		k = other
		k=list(k)
	data.append(k + c)
	d=d+1
	f=[]
	c=[]
print data
query7 = 1
query6 = ("create table final (id int(10), dept varchar(40), name varchar(40), title varchar(40), salary decimal (10,5), first varchar(10), gender varchar(2), percent decimal(10,5), percentile decimal(10,5), rank int(10), first2 varchar(10), gender2 varchar(2), percent2 decimal(10,5), percentile2 decimal(10,5), rank2 int(10));")
cursor.execute(query6)
for line in data:
	moop = len(line)
	if moop < 15:
		line.append(None)
		line.append(None)
		line.append(None)
		line.append(None)
		line.append(None)
	print line[8]
	query7 = ("insert into final (id, dept, name, title, salary, first, gender, percent, percentile, rank, first2, gender2, percent2, percentile2, rank2) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" % (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14]))
	cursor.execute(query7)
cursor.close()
cnx.close()