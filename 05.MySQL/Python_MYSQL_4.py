import pymysql


conn = pymysql.connect(host='localhost', user ='Lucas', password='96669901',
					  db='sqlclass_db', charset='utf8' )


curs = conn.cursor()

sql = '''INSERT INTO customer(name, category, region)
		VALUES(%s,%s,%s)'''

curs.execute(sql,('홍길동',1,'서울'))
curs.execute(sql,('이연수',2,'서울'))
conn.commit()

print('INSERT 완료')

curs.execute('select * from customer')
rows = curs.fetchall()
print(rows)


curs.close()
curs.close() 