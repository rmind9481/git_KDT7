
import requests
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
# import collections 

# collections.Callable = collections.abc.Callable 


def naver_weather_find(soup):
    '''
    find() 함수 사용 
    '''
    #--------------------------------------------------------
    # 위치 
    #--------------------------------------------------------
    city_address = soup.find('div', {'class':'title_area _area_panel'})
    city = city_address.find('h2', {'class':'title'}).text # 대구광역시 
    current_location = city_address.find('span', {'class':'select_txt_sub'}).text 
    current_location = current_location[:-3]
    print(f'{city}: {current_location}')

    #--------------------------------------------------------
    # 현재 날씨 정보 
    #--------------------------------------------------------
    weather_data = soup.find('div', {'class':'weather_info'})
    # 현재 온도 
    weather_temp = weather_data.find('div', {'class': 'temperature_text'}).text.strip()
    print('현재 온도: ', weather_temp)
    # 날씨 상태 
    weather_status = weather_data.find('span', {'class':'weather before_slash'}).text
    print('날씨 상태: ', weather_status)

    #--------------------------------------------------------
    # 미세 먼지, 초미세 먼지, 자외선, 일출
    #--------------------------------------------------------
    # class="today_chart_list"
    air = soup.find('ul', {'class':'today_chart_list'})

    air_all_info = air.find_all('li', {'class':'item_today'})
    print('[공기 상태] ')
    for info in air_all_info:
        print(info.text.strip())

    #--------------------------------------------------------
    # 시간대별 날씨 및 온도 
    #--------------------------------------------------------
    weather_time = soup.find_all('li', {'class': '_li'})
    print('-----------------------')
    print('시간대별 날씨 및 온도')
    print('-----------------------')
    for i in weather_time:
        print(i.text.strip())



def naver_weather_select(soup):
    '''
    select() 함수 사용 
    '''
    #--------------------------------------------------------
    # 위치 
    #--------------------------------------------------------
    # 방법 1: 상위 tag 선택 후 검색 범위를 줄여나감 
    # class속성 값이 여러 개인 경우 '.'으로 여러 개 연결 
    #city_location = soup.select_one('div.title_area._area_panel > h2.title').text    
    city_address = soup.select_one('div.title_area')
    city = city_address.select_one('h2.title').text
    current_location = city_address.select_one('span.select_txt_sub').text

    # 방법 2
    '''
    city = soup.select_one('h2.title').text    
    current_location = soup.select_one('span.select_txt_sub').text
    '''
    current_location = current_location[:-3]    
    print(f'{city}: {current_location}')

    #--------------------------------------------------------
    # 현재 날씨 정보 
    #--------------------------------------------------------
    weather_data = soup.select_one('div.weather_info')
    weather_temp = weather_data.select_one('div.temperature_text').text.strip()
    #weather_temp_title = weather_data.select_one('div.temperature_text span.blind').text.strip()
    print(f'{weather_temp}')
    # 날씨 상태 
    #weather_status = soup.select_one('div.temperature_info span.weather').text
    weather_status = soup.select_one('span.weather.before_slash').text
    print(f'날씨 상태: {weather_status}')

    #--------------------------------------------------------
    # 미세 먼지, 초미세 먼지, 자외선, 일출
    #--------------------------------------------------------
    # air_quality 항목 
    air_quality = soup.select_one('ul.today_chart_list')
    air_info = air_quality.select('li.item_today')
    print('[공기 상태]')
    for info in air_info:
        print(info.text.strip())
    #--------------------------------------------------------
    # 시간대별 날씨 및 온도 
    #--------------------------------------------------------
    #weather_time = soup.select('li._li')
    weather_time = soup.select('dl.graph_content')
    print('-----------------------')
    print('시간대별 날씨 및 온도')
    print('-----------------------')
    for i in weather_time:
        print(i.text.strip())





def main():

    # 방법 1: requests 모듈 사용

    # 한글 encode('ascii') 문제 발생 
    # url='https://search.naver.com/search.naver?query=대구+날씨'
    # html = requests.get(url)
    # soup = BeautifulSoup(html.text, 'html.parser')


    #city = input('지역명을 입력하세요(대구, 서울 등): ')
    # city = '대구'
    # # 방법 2: 한글 깨지는 문제 때문에 quote('한글') 사용
    # #query = quote(f'{city}+날씨')
    query = quote('대구날씨')
    url='https://search.naver.com/search.naver?query=' + query

    html = urlopen(url)
    soup = BeautifulSoup(html.read(), 'html.parser')

    # find() 함수를 사용한 검색 
    #naver_weather_find(soup)

    # select() 함수를 사용한 검색 
    naver_weather_select(soup)


main()