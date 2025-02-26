import pandas as pd

dust = pd.read_excel('../Day4_airquality/dust_hour.xlsx')


print('결측치 개수 확인하기')
# NaN 값을  포함 하는 행 추출
print(dust[dust.isna().any(axis=1)])

print('결측치 채우기')

dust.ffill(inplace= True)
print(dust.isnull().sum())


# 이전 결측치 index
print(dust.iloc[84:86])
