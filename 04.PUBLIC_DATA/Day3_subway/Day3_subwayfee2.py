import csv
import matplotlib.pyplot  as plt
import koreanize_matplotlib



file = open('../Data/3Day/subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(file)
header = next(data)

min_rate = 100
min_row = []
min_total_count = 0


for row in data :
	for i in [4,6]:
		row[i] = int(row[i]) # 4,6 컬럼 값을 정수로 변환

	total_count = row[4] + row[6] # 유임승차수 + 무임승차수
	
	# 무임승차 인원이 0인경우 건너뜀 그리고 10만명 이상
	if (row[6] != 0) and (total_count >= 10000):
		# 무임승차 (%) = (무임 승차수 x 100) / (유임 승차 수 + 무임 승차 수 )
		rate = row[4]/ total_count

		if rate <= 0.5:
			print(row, round(rate,2))
			if rate < min_rate:
				min_rate = rate
				min_row = row
				min_total_num = total_count
	
file.close()


print()
print(f'유임 승차 비율이 가장 낮은 역:	{min_row[3]}')
print(f'전체 인원:{min_total_count:,}명,'
						f'유임승차인원:{min_row[4]:,}명,'
						f'유임승차비율:{round(min_rate*100,	1)}%') 
plt.title(min_row[3]	+	"역 유,무임 승차 비율")
label	=	['유임승차',	'무임승차']
values	=	[min_row[4],	min_row[6]]
plt.pie(values,	labels=label,	autopct='%.1f%%')
plt.legend(loc=2)
plt.show()

