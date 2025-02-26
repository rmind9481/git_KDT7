import pymysql


def	create_table(conn,cur):
	try:
		query1	=	'DROP	TABLE	IF	EXISTS	customer'
		query2	=	"""
		CREATE	TABLE	customer
		(name	varchar(10),	
		category	smallint,	
		region	varchar(10))
		"""
		cur.execute(query1)
		cur.execute(query2)
		conn.commit()
		print('Table	생성 완료')
	except	Exception	as	e:
		print(e)


def	main():
	conn =pymysql.connect(host='localhost',user='Lucas',password='96669901',db='sqlclass_db',charset='utf8')
	cur	=conn.cursor()
	#테이블 생성 함수 호출
	create_table(conn,	cur)
	#연결 종료
	cur.close()
	conn.close()
	print('Database	연결 종료')

main()