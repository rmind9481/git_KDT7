from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

store_list = []

num =1 

for i in range(48):
	html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={num}&sido=&gugun=&store=')

	soup = BeautifulSoup(html,'html.parser')
	num +=1
	coffee_page = soup.find('tbody')
	
	

	tag_tr = coffee_page.find_all('tr')
	for i in  tag_tr:
		tag_td = i.find_all('td')
		
		#print(tag_td[0])
		#print(len(tag_td))
		
		#print(tag_td[0].text.strip())

		# 지역
		regin = tag_td[0].text.strip()


		#print(tag_td[1].text.strip())

		# 매장이름
		store_name = tag_td[1].text.strip()
		#print(tag_td[3].text.strip())

		# 매장 주소
		store_address = tag_td[3].text.strip()
		#print(tag_td[4].text.strip())
		#print(tag_td[5].text.strip())

		# 매장 번호
		store_number = tag_td[5].text.strip()
		
		# 순서 매장이름 지역 주소 전화번호
		store_list.append([len(store_list)+1, store_name, regin, store_address,store_number]) 

# 전체 매장 확인
#print(len(store_list))
#print(store_list)

store_list_df = pd.DataFrame(data=store_list ,columns=['순서','매장이름','지역','주소','전화번호'])

store_list_df.set_index('순서',inplace=True)
file = '../EXAM/coffee.csv'

print(store_list_df)

store_list_df.to_csv(file)





