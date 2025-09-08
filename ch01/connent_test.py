import pymysql

#1. connect
conn = pymysql.connect(host='localhost', user='sunye', password='q1w2e3', db='shopping_db1')

#2. susor
cur = conn.cursor()
#3. writing query
cur.execute('select * from customer')
#4. check
result = cur.fetchall()
ages = [row[2] for row in result if row[3] == '경기']
avg_age = sum(ages) / len(ages)
print(int(avg_age))
#5. end(byebye connect)
cur.close()
conn.close()
