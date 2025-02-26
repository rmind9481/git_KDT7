import pandas as pd
import matplotlib.pyplot as plt

weathr_df = pd.read_csv('../Data/deagu-utf8.csv', encoding='utf-8-sig')

print(weathr_df.columns)
print(weathr_df['날짜'].dtype)



weathr_df.columns=['날짜', '지점', '평균기온', '최저기온', '최고기온']
print(weathr_df.columns)                   

weathr_df['날짜'] = pd.to_datetime(weathr_df['날짜'], format='%Y-%m-%d')
print(weathr_df['날짜'].dtype)


print(weathr_df.head(5))
print(weathr_df.shape)

num_rows = weathr_df.shape[0]

num_missing = num_rows - weathr_df.count()
print(num_missing)


weathr_df = weathr_df.dropna(axis=0)

print(weathr_df.count())
print(weathr_df.head(5))


weathr_df.to_csv("daegu-utf8-df.csv", index=False, mode='w', encoding='utf-8-sig')



print('특정 연도 와 달의 최고, 최저 기온 평균값 계산')

year_df = weathr_df[weathr_df['날짜'].dt.year == 2024]
month_df = year_df[year_df['날짜'].dt.month == 1]

print(month_df.head())


# 최고, 최저 기온 평균값 계산

max_temp_mean = round(month_df['최고기온'].mean(), 1)
min_temp_mean = round(month_df['최저기온'].mean(), 1)

print(f'2023년 8월 최저기온 평균 :{min_temp_mean}, 최고기온 평균 :{max_temp_mean}')





