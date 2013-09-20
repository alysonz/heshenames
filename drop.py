import mysql.connector
cnx = mysql.connector.connect(user='alyson', password='thetempleofwhollyness', host='localhost', database='heshenames')
cursor = cnx.cursor()
query6 = ("drop table doagender;")
cursor.execute(query6)
cursor.close()
cnx.close()
