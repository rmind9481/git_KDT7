import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib 


# csv 자료 읽기

file = open('../Data/2Day/gender.csv', encoding='euc_kr')
data = csv.reader(file)
next(data)

# 빈 리스트에 대구광역시 인구 넣기


male_count = []
female_count = []
city_name_list =  []

# 대구 광역시 뽑아내기
city = '대구광역시'



# 남 
# 여 저장하기

for row in data:
	#print(row[0])
	city_name = re.split('[()]',row[0])
	# 대구광역시를 인것들만 선별
	city_name = city_name[0].split()
	
	while city == city_name[0]:
		
		# 자릿수 문자열 , 제거 및 숫자로 변환 
		male_count.append(int(row[104].replace(',','')))
		print(male_count)
		female_count.append(int(row[207].replace(',','')))
		city_name_list.append(city_name)
		break 
# city_name 리스트에 담긴 값을 분해후 합친다.
merged_locations = [' '.join(city_name_list) for city_name_list in city_name_list]

population =[]
for i in range(len(city_name_list)):
	print(f"{merged_locations[i]} : (남 :{male_count[i]}, 여 :{female_count[i]})")
	population.extend([(male_count[i], female_count[i])] )

plt.figure(figsize=(15,15))
print(population)
color=['cornflowerblue','tomato']
i =1

while i <= 10:

	for j in range(len(population)):
		plt.subplot(2,5,i)
		plt.pie(population[j], labels=['남성','여성'],	autopct='%.1f%%',	colors=color,	startangle=90)
		plt.title(merged_locations[j])
		i+=1	
	
plt.suptitle("대구광역시 구/군별 남녀 인구비율", fontsize = 20)
plt.show()
# 파이차트로 각각 출력
# subplots 이용해서 5x2 형태


