import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib


with open('../Data/3Day/subwaytime.csv', encoding='utf-8-sig') as f:
	data = csv.reader(f)
	next(data)
	next(data)


	max_num	= [0]*7
	max_station_name =['']*7
	station_name =['']*7

	check_station = ["1호선","2호선","3호선","4호선","5호선","6호선","7호선"]
	
# [1] 호선명 [3] 역이름 [11] [13] 하차

	for	row	in	data:
		for i in range(1,8):
		# 1~7호선 선별
			if  ('공항철도'not in row[1]) and  ((str(i)+'호선') in row[1]):
				row[5:]	=	map(int,row[5:])
			# 1~7호선 선별
					#print(row[1])
					#하차 이후 숫자로 변경
					# 7~9시 총 하차인원 합 
				passenger_num = sum(row[11:15:2])
	
				if  check_station[i-1] in row[1] and (passenger_num > max_num[i-1]) :
					max_num[i-1] = passenger_num
					station_name[i-1] = row[1]+row[3]
					max_station_name[i-1] ='출근 시간대' +row[1]+' 최대 하차역'+' '+row[3] +'역'

					

	for i in range(len(max_station_name)):
		
		print((f'{max_station_name[i]} 하차인원: {max_num[i]:,}'))


plt.bar(max_station_name,max_num)
plt.xticks(range(7), labels=station_name,	rotation=245)
plt.suptitle('출근시간대 노선별 최대 하차 인원 및 하차역\n',	size=20)
plt.tight_layout()	
plt.show()


