import csv

file = open('../Data/3Day/subwayfee.csv', encoding='utf-8-sig')

data = csv.reader(file)

header = next(data)
max_rate = 0 # <= 최대값을 찾기 위한 기준값값
rate = 0
#print(header)



# =============================================================
# 데이터 위에 헤더 정보 5개 확인인
# i = 1 

# for row in data: 
# 	print(row)
# 	if i > 5:
# 		break
# 	i +=1

# =============================================================


for row in data :
	for i in range(4,8,2):
		row[i] = int(row[i]) # 4,6 컬럼 값을 정수로 변환

	total_count = row[4] + row[6] # 유임승차수 + 무임승차수
	
	# 무임승차 인원이 0인경우 건너뜀 그리고 10만명 이상
	if (row[6] != 0) and (total_count > 100000):
		# 무임승차 (%) = (무임 승차수 x 100) / (유임 승차 수 + 무임 승차 수 )
		rate = row[4]/ total_count
	# if row[6] == 0:
	# 	print(row)
		if rate > max_rate:
			max_rate = rate
			max_row = row
			max_total_num = total_count
			print(f" {max_row[1]},{max_row[3]},전체 인원: {max_total_num:,}명,"
		 			f"유임승차인원:	{max_row[4]:,}명,"
					f"유임승차 비율: {round(max_rate *100,1):,}%")
			# 변화 되는 과정 디버깅0
			#print(row, round(rate, 2), '%')


# 마지막 결과만 출력
# print(max_rate, max_row)

file.close()


