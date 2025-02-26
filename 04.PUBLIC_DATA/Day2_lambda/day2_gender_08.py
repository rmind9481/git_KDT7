import csv
import matplotlib.pyplot as plt
import platform
import math
import koreanize_matplotlib


def draw_scatter(city, male_list , femele_list, bubble_size_list):
	plt.figure(figsize=(8,4), dpi=100)
	
	plt.scatter(male_list, femele_list, s=bubble_size_list, c=range(101), alpha= 0.5, cmap='jet')
	plt.colorbar()

	# 추세선 추가 (녹샌 점선)
	plt.plot(range(max(male_list)), range(max(male_list)), 'g--')


	plt.title(city + "지역의 남녀 인구수 비교")
	plt.xlabel("남성 인구수")
	plt.ylabel('여성 인구수')
	plt.show()

def calculate_population():
	file = open('../Data/2Day/gender.csv',encoding='euc_kr')
	data = csv.reader(file)

	male_list = []
	female_list = []
	bubble_size_list = []

	city = input('찾고 싶은 지역의 이름을 입력하세요')


	for row in data:
		if city in row[0]:
			for i in range(106,207):
				male_num = int(row[i].replace(',',''))
				female_num =  int(row[i+103].replace(',',''))

				# 버블의 사이즈 조절
				bubble_size_list.append(math.sqrt(male_num +female_num))
				male_list.append(male_num)
				female_list.append(female_num)

			break

	file.close()

	print(f'[여성 인구]: {female_list}')
	print(f'[남성 인구]: {male_list}')
	draw_scatter(city, male_list, female_list, bubble_size_list)

calculate_population()