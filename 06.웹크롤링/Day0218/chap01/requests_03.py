from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import requests

def use_urlopen(url):
	urlrequest = Request(url, headers={'User-Agent':'Mozilla/5.0'})
	html = urlopen(urlrequest)

	soup = BeautifulSoup(html.read().decode('utf-8'),'html.parser')
	print(soup)


def use_requests(url):
	response = requests.get(url, headers={'Uesr-Agent': 'Mozilla/5.0'})
	soup = BeautifulSoup(response.text, 'html.parser')
	print(soup)


def main():
	melon_url = 'https://www.melon.com/chart/index.htm'
	# HTTP requrest 패킷 생성 : Request()
	use_urlopen(melon_url)
	use_requests(melon_url)

main()