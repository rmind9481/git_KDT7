import csv
import matplotlib.pyplot as plt
import re 
import koreanize_matplotlib




def parse_district_name(city) :
    '''
    행정구역, 명칭에서 숫자 부분을 제거함
    -
    '''
    city_name =	re.split('[()]',city)
	#print(city_name)
    return	city_name[0]

def	print_population(population):
	'''
		특정 지역의 인구 현황을 한 줄에 10개씩 화면에 출력함
    '''
	for	i in	range(len(population)):
		print(f'{i:3d}세:	{population[i]:4d}명',	end=' ')
		if	(i +1)%	10 == 0:
		    print()

def draw_population(city_name, population_list):
	
    plt.title(f'{city_name} 인구현황')
    plt.xlabel('나이')
    plt.ylabel('인구수')
    plt.bar(range(101), population_list)
    plt.xticks(range(0, 101, 10))
    plt.show()

def get_population(city):
	file = open('../Data/2Day/age.csv', encoding='euc_kr')
	data = csv.reader(file)
	next(data)
	population_list = []
	full_district_name = ''
	for row in data:
		if city in row[0]:
			full_district_name = parse_district_name(row[0])
			for data in row[3:]:
				data = data.replace(',','')
				population_list.append(int(data))
			break
	
	file.close()
	print_population(population_list)
	draw_population(full_district_name,	population_list)
	
city = input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요:	')
get_population(city)