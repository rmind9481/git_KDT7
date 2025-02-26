import pandas as pd

data = './coffee.csv'

coffee_df = pd.read_csv(data)

print(coffee_df )


coffee_iniput_df = pd.DataFrame(columns=['번호','매장이름','주소','전화번호'])

print(coffee_iniput_df)
print(coffee_df.columns)



while True :


	# 사용자 입력 받기
	city = input('검색할 매장의 지역을 입력하세요: ').strip()

	# 무한반복 루트 탈출하기
	if city == 'quit':
		break

	num = 0
	for i in coffee_df.index:

		if city in coffee_df.loc[i, '지역']:  # '지역' 컬럼에 city가 포함되어 있는지 확인
			num += 1
			#딕셔너리 형태로 데이터 넣기
			new_row = {
				'번호': num,
				'매장이름': coffee_df.loc[i, '매장이름'],
				'주소': coffee_df.loc[i, '주소'],
				'전화번호': coffee_df.loc[i, '전화번호']
			}
			coffee_iniput_df = pd.concat([coffee_iniput_df, pd.DataFrame([new_row])], ignore_index=True)

			continue
	# 결과 출력
	coffee_iniput_df.set_index('번호')
	print(coffee_iniput_df)

		
	coffee_iniput_df = coffee_iniput_df.iloc[0:0]
	num = 0