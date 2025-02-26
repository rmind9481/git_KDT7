from bs4 import BeautifulSoup  # BeautifulSoup 라이브러리를 가져옴 (HTML 파싱 용도)
from selenium import webdriver  # Selenium 라이브러리를 가져옴 (웹 자동화 용도)

driver = webdriver.Chrome()  # Chrome 브라우저를 실행하는 드라이버 객체 생성
driver.get('https://blog.naver.com/swf1004/221631056531')  # 해당 URL의 웹페이지를 엶

driver.switch_to.frame('mainFrame')  # 'mainFrame'이라는 iframe 내부로 이동

html = driver.page_source  # 현재 페이지의 HTML 소스를 가져옴
soup = BeautifulSoup(html, 'html.parser')  # BeautifulSoup을 사용하여 HTML을 파싱

# 'se-module' 클래스를 가진 모든 div 태그 찾기
results = soup.find_all('div', {'class': 'se-module'})  

result1 = []  # 추출된 텍스트를 저장할 리스트 생성
for result in results:  # 찾은 모든 요소에 대해 반복
    remove_carriage_str = result.text.replace('\n', '')  # 줄바꿈 문자를 제거하여 가독성을 높임
    print(remove_carriage_str)  # 변환된 텍스트 출력
    result1.append(remove_carriage_str)  # 리스트에 변환된 텍스트 추가
