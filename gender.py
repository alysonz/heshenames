import mysql.connector
import re
cnx = mysql.connector.connect(user='alyson', password='thetempleofwhollyness', host='localhost', database='heshenames')
cursor = cnx.cursor()
cursor.execute("create table doagender13 (id int(10), dept varchar(40), name varchar(40), title varchar(40), salary decimal (10,5), first varchar(20), genderPercent decimal(10,5), gender varchar(1), percent decimal(10,5), percentile decimal(10,5), rank int(10), first2 varchar(20), genderPercent2 decimal(10,5), gender2 varchar(1), percent2 decimal(10,5), percentile2 decimal(10,5), rank2 int(10))")
cursor.execute("insert into doagender13(id, dept, name, title, salary, first, genderPercent, gender, percent, percentile, rank, first2, genderPercent2, gender2, percent2, percentile2, rank2) select id, dept, name, title, salary, first, ((percent*3200000)/((percent2*3000000)+(percent*3200000)))*100, gender, percent, percentile, rank, first2, ((percent2*3000000)/((percent2*3000000)+(percent*3200000)))*100, gender2, percent2, percentile2, rank2 from final13")
cnx.commit()
print 'Success!'
cursor.close()
cnx.close()
