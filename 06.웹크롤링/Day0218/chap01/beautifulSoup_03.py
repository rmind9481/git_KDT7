from urllib.request	import urlopen
from urllib.error import HTTPError
from bs4	import BeautifulSoup
def get_title(url, tag):
	try: 
		html = urlopen(url)
		bs = BeautifulSoup(html.read(), 'html.parser')
		value = bs.find(tag)
	except HTTPError as e:
		return None
	except AttributeError as e:
		print(f'AttributeError{e}')
		return None
	else:
		return value
	
tag='h2'
url =	'http://www.pythonscraping.com/pages/page1.html'
value	=	get_title(url,	tag)
if value	==	None:
	print(f'{tag} could	not	be found')
else:
	print(value)