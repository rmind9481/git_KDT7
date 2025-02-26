from urllib.request	import	urlopen
from bs4 import	BeautifulSoup
html = urlopen('https://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html,	'html.parser')

table_tag =	soup.find('table',	{'id':	'giftList'})
print('children	개수:',len(list(table_tag.children)))


# 트리이동 : 자손
desc = soup.find('table', {'id':'giftList'}).descendants
list_desc = list(desc)

print('descendants 개수: ', len(list_desc))
index=0

for	child in table_tag.children:	
    index	+=	1
    print(f"[{index}]:	{child}")
    print('-'	*	30)

# 트리이동 : 자손

for tag in list_desc:
    print(tag)

for	child in list_desc:	
    index	+=	1
    print(f"[{index}]:	{child}")
    print('-'	*	30)


# ---------------------------------------------------------
# 형재 : next_siblings 속성
# ---------------------------------------------------------

for sibling in soup.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)
    print('-'*50)


print('previous_siblings')
for sibling in soup.find('tr',{'id':'gift2'}).previous_siblings:
    print(sibling)


img1 = soup.find('img',{'src':'../img/gifts/img1.jpg'})
prev_text = img1.parent.previous_sibling.text
print(prev_text)