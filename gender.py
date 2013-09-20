import mysql.connector
import re
cnx = mysql.connector.connect(user='alyson', password='thetempleofwhollyness', host='localhost', database='heshenames')
cursor = cnx.cursor()
cursor.execute("create table doagender select id, dept, name, title, salary, first, ((percent*3200000)/((percent2*3000000)+(percent*3200000)))*100, gender, percent, percentile, rank, first2, ((percent2*3000000)/((percent2*3000000)+(percent*3200000)))*100, gender2, percent2, percentile2, rank2 from final")
cnx.commit()
print 'Success!'
cursor.close()
cnx.close()
