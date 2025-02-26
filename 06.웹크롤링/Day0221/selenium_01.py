
#import selenium
from selenium import webdriver 
import time 
'''
	selenium	4.xx	버전은 chromedriver를 별도로 다운로드할 필요 없음
	- selenium	4.23.1
'''

driver	= webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


#print(selenium.__file__)
print(f'title:{driver.title}')
print(driver.page_source)
time.sleep(10)
driver.quit()