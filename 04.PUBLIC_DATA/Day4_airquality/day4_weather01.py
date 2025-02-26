import pandas as pd
from tabulate import tabulate
from datetime	import timedelta
import	seaborn	as	sns
import	matplotlib.pyplot as plt
import koreanize_matplotlib

weather = pd.read_excel('../Data/4Day/weather.xlsx')
dust = pd.read_excel('../Day4_airquality/dust_hour.xlsx')

# 데이터 읽어 오기
print(tabulate(weather.head(), headers='key', tablefmt='pretty'))

print(weather.info())

# 컬럼명 바꾸기
weather.drop(['지점','지점명'], axis=1, inplace=True)

weather.columns  = ['date',	'temp',	'wind',	'rain',	'humidity']
# 테이블 확인
print(tabulate(weather.head(), headers='keys', tablefmt='psql'))

# 날씨 결측치 확인

print('날씨 데이터 결측치 개수 확인')
print(weather.isna().sum())

print('강수량이 0인 항목을 0.01로 변경')
weather['rain']	=	weather['rain'].replace(0,	0.01)
print(weather['rain'].value_counts())

print('dust,weather의 크기 확인')
print('dust.shape',	dust.shape)
print('weather.shape',	weather.shape)


# 미세먼지 데이터의 마지막 부분 확인
print(dust.iloc[716:])

# 날씨 데이터의 마지막 부분확인
print(weather.iloc[716:])



# 데이터 병합하기

print('dust,weather	데이터프레임 merge')
merged_df =	pd.merge(dust,weather,how='inner',on='date')
print(tabulate(merged_df.head(),	headers='keys',	tablefmt='psql'))


# 병합된 데이터 프레임 크기 확인
print(merged_df.shape)


merged_df.to_excel('dust_weather.xlsx',	index=False)
print(merged_df.corr())



print('미세먼지(PM10)과 상관관계 분석')
corr =	merged_df.corr() #corr()	:DataFrame을 리턴
print(corr['PM10'].sort_values(ascending=False)) #내림차순 정렬

merged_df.hist(column=['so2','co','o3','no2','PM10','PM2.5','temp','wind','rain','humidity'],bins=50,figsize=(20,15))
plt.show()

plt.figure(figsize=(15,	10))
sns.barplot(x=merged_df['date'].dt.day,	y='PM10', data=merged_df,errorbar=None)
plt.title("날짜별 PM10	농도",	fontsize=20)
plt.show()

# 막대그래프
plt.title("날짜별 PM10/PM2.5	농도",	fontsize=12)
plt.plot(merged_df['PM10'],	label='PM10')
plt.plot(merged_df['PM2.5'],	label='PM2.5')
plt.legend()
plt.show()

# PM10과 PM2.5 농도 비교
plt.title("날짜별 PM10/PM2.5	농도",	fontsize=12)
merged_df['PM10'].plot(kind='line',	x='date')
merged_df['PM2.5'].plot(kind='line',	x='date')
plt.legend()
plt.show()


#히트맵 작성
plt.figure(figsize=(10,	10))
sns.heatmap(data=corr,	annot=True,	fmt='.2f')
plt.show()


# 산점도(PM10과 PM2.5)
plt.figure(figsize=(15,	10))
x	=merged_df['PM10']
y	=merged_df['PM2.5']
plt.plot(x,	y,	marker='o',	linestyle='none',	color='red',	alpha=0.5)
plt.title('PM10	vs.	PM2.5')
plt.xlabel('PM10')
plt.ylabel('PM2.5')
plt.show()