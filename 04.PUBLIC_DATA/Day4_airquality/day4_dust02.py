import pandas as pd
from tabulate import tabulate
from datetime	import timedelta

# dust.xlsx
dust = pd.read_excel('../Data/4Day/dust.xlsx')

# 데이터 읽어 오기
print(tabulate(dust.head(), headers='key', tablefmt='pretty'))

print(dust.info())

# 컬럼명 바꾸기
dust.rename(columns={'날짜':'date',	'아황산가스':'so2',
							'일산화탄소':'co',	'오존':'o3',
							'이산화질소':'no2'}, inplace=True)


# 테이블 확인
print(tabulate(dust.head(), headers='keys', tablefmt='psql'))


# print('[date]자료형(object)을 datetime 타입으로 변경')
# dust['date']	=	pd.to_datetime(dust['date'],	format='%Y-%m-%d	%H')



def zerofrom24(datestring):
	'''
		24시로 표현된 값을 익일 00로 변환 
	'''

	try : 
		return pd.to_datetime(datestring, format ='%Y-%m-%d %H' )
	except:
		datestring =datestring[:11]	+	'00'
		return pd.to_datetime(datestring,format='%Y-%m-%d %H')+timedelta(days=1)
	
dust['date']=dust['date'].apply(zerofrom24)
print(dust.info())
print(dust[dust['date'].dt.day==5])

dust.to_excel('dust_hour.xlsx',	index=False)
print(dust.info())