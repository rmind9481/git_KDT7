import pymysql
import pandas as pd
import pymysql.cursors

conn = pymysql.connect(host='localhost', user='Lucas', password='96669901' ,
						db='sakila', charset='utf8')


#cur = conn.cursor()
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from language')
rows = cur.fetchall() # 모든 데이터를 가져옴 => DataFrame 형태
print(rows)

language_df = pd.DataFrame(rows)
print(language_df)


print(language_df['name'])
cur.close()
conn.close()

