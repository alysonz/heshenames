#def drop(tableName, dbName):
import MySQLdb
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
cursor.execute("drop table flaggedEmployees")
db.commit()
cursor.close()
db.close()
