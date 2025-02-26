import requests  # URL 요청을 보내고 데이터를 가져오는 모듈
from	bs4	import	BeautifulSoup
from urllib.request import urlopen # URL 요청을 보내고 데이터를 가져오는 모듈

html	=	requests.get('https://finance.naver.com/sise/sise_market_sum.naver')
soup	=	BeautifulSoup(html.text,	'html.parser')

KOSPI_tbody = soup.find('tbody')
tag_tr	= KOSPI_tbody.find_all('tr')

Kospi_list= []
# 코스피 이름/ 링크 리스트에 저장
for i in tag_tr:
	stock_title = i.find('a',{'class','tltle'})
	stock_price = i.find_all('td' ,{'class','number'})
	

	if stock_title and stock_price:
		stock_name = stock_title.text.strip()
		stock_link = 'https://finance.naver.com'+ str(stock_title.attrs['href'])

		현재가 = stock_price[0].text.strip()
		
		Kospi_list.append([stock_name,stock_link,현재가])

	#	– 종목명, 종목코드, 현재가, 전일가, 시가, 고가, 저가

# if stock_title and stock_price:
#         stock_name = stock_title.text.strip()
#         stock_link = BASE_URL + stock_title["href"]
#         price = stock_price.text.strip()

#         stock_list.append((stock_name, stock_link, price))
print('=========== 코스피 top 10 ================')
for i in Kospi_list[:10]:
	print()
	print(f'종목명 :{i[0]}')
	print(f'링크 :{i[1]}')
	print(f'현재가 :{i[2]}')

# name   	
#종목명, 종목코드, 현재가, 전일가, 시가, 고가, 저가