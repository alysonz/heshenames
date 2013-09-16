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
		f = that
	query5 = ("select * from doafull where id=%s;" %(d))
	cursor.execute(query5)
	for other in cursor:
		k = other
	data.append(k + f)
#	query = ("select id from doanames where id=%s;" %(d))
#	cursor.execute(query)
#	for name in cursor:
		#then use id to find full emp info within doafull
#		query1 = ("select * from doafull where id=%s;" %(name))
#		cursor.execute(query1)
#		for thing in cursor:
			#print full emp info
#			print thing
	d=d+1
cursor.close()
cnx.close()
l=[]
print data
for line in data:
	for item in line:
		l.append(item)
print l
for item in l:
	item= re.sub('u', '', item)
#heshenames.writelines(l)
#query2 = ("select * from heshe where rank=1")
#cursor.execute(query2)
#for rank in cursor:
#	print rank
