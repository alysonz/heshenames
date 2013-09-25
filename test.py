# WRITE SCRIPT/QUERY TO AVERAGE MALE/FEMALE SALARY FOR EVERY DISTINCT TITLE IN EVERY AGENCY AND FLAG TITLE/AGENCY W/LARGISH MALE/FEMALE SALARY DIFFERENCE
import MySQLdb
import re
db = MySQLdb.connect(user='alyson', passwd='thetempleofwhollyness', db='heshenames')
cursor= db.cursor()
#find all distinct departments
cursor.execute("select salary from doagender;")
for line in cursor:
	faggot = line[0] + 500
	print faggot
#db.commit()
print 'Success!'
cursor.close()
db.close()
