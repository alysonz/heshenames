import mysql.connector
cnx = mysql.connector.connect(user='alyson', password='thetempleofwhollyness', host='localhost', database='heshenames')
cursor = cnx.cursor()
d = 1
while d < 10:
	query = ("select * from doanames where id=%s;" % (d))
	cursor.execute(query)
	for name in cursor:
		print name
	d=d+1
query2 = ("select * from heshe where rank=1")
cursor.execute(query2)
for rank in cursor:
	print rank
cursor.close()
cnx.close()
