import pymysql


conn = pymysql.connect(host='localhost', user ='Lucas', password='96669901',
					  db='sqlclass_db', charset='utf8' )


curs = conn.cursor()

dql = '''
	UPDATE customer
	SET regin = '서울특별시'
	WHERE region = '서울'
'''
print('update 완료')

sql = 'DELETE FROM customer WHERE name=%s'
curs.execute(sql,'홍길동')
print('delete 홍길동')

conn.commit()
curs.close()
conn.close()