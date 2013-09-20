import mysql.connector
import re
cnx = mysql.connector.connect(user='alyson', password='thetempleofwhollyness', host='localhost', database='heshenames')
cursor = cnx.cursor()
d = 1
f = 0
m = 0
while d < 10:
	cursor.execute("select * from final where id=%d" %(d))
	for line in cursor:
		print line
	cursor.execute("select ((percent*3200000)/((percent2*3000000)+(percent*3200000)))*100, gender from final where id=%d" %(d))
	for line in cursor:
		f = line
	cursor.execute("select ((percent2*3000000)/((percent2*3000000)+(percent*3200000)))*100, gender2 from final where id=%d" %(d))
	for line in cursor:
		m = line
	cursor.execute("s"
	print "done"
#		f.append(that)
#		f=list(f)
	#restore lists in list f as items in list c.
#	for line in f:
#		for stuff in line:
#			c.append(stuff)
#query6 = ("create table final (id int(10), dept varchar(40), name varchar(40), title varchar(40), salary decimal (10,5), first varchar(10), gender varchar(2), percent decimal(10,5), percentile decimal(10,5), rank int(10), first2 varchar(10), gender2 varchar(2), percent2 decimal(10,5), percentile2 decimal(10,5), rank2 int(10))")
#cursor.execute(query6)
#	if len(line) < 15:
#		line.extend(['none', 'none', '0.0', '0.0', '0'])
#	query7 = ("insert into final (id, dept, name, title, salary, first, gender, percent, percentile, rank, first2, gender2, percent2, percentile2, rank2) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14]))
#	cursor.execute(query7)
	d=d+1
#cnx.commit()
print 'Success!'
cursor.close()
cnx.close()
