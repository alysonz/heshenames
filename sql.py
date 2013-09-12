import mysql.connector
cnx = mysql.connector.connect(user='alyson', password='thetempleofwhollyness', host='localhost', database='heshenames')
cursor = cnx.cursor()
d = 1
f = 1
n = 1
while d < 10:
#first take id from doanames 1-10
	query3 = ("select name from doanames where id=%s;" %(f))
	cursor.execute(query3)
	for name in cursor:
		n = name
	query4 = ("select * from heshe where name='%s';" %(n))
	cursor.execute(query4)
	for name in cursor:
		name
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
query2 = ("select * from heshe where rank=1")
cursor.execute(query2)
for rank in cursor:
	print rank
cursor.close()
cnx.close()
