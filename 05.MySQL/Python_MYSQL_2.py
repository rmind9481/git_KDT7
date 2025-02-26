import pymysql
import pandas as pd


conn = pymysql.connect(host='localhost', user='Lucas', password='96669901' ,
						db='sakila', charset='utf8')

cur	=	conn.cursor(pymysql.cursors.DictCursor)

query ='''
SELECT c.first_name, c.last_name, c.email
FROM customer	as	c
	INNER JOIN rental as r
	ON	c.customer_id =	r.customer_id
WHERE date(r.rental_date) = %s
'''

cur.execute(query, ('2005-06-14'))


rows = cur.fetchall()
result_df = pd.DataFrame(rows)
print(result_df)
cur.close()
conn.close()
