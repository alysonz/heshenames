import mysql.connector
cnx = mysql.connector.connect(user='alyson', password='thetempleofwhollyness', host='localhost', database='heshenames')
cursor = cnx.cursor()
query = ("SELECT name, salary FROM doafull")
cursor.execute(query)
for (name, salary) in cursor:
	print name + " " + salary
cursor.close()
cnx.close()
