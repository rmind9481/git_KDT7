html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>
        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="external_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')

# 직접 접근 방법
print(soup)
print(soup.title) # <title> 태그 전체를 가져옴
print(soup.title.parent) # <title> 태그의 텍스트만 리턴
print(soup.title.get_text()) # .string, .text(예전 버전) 와 동일한 기능

print(soup.body)

# h1 태그 접근
# 직접 접근 방법
print(soup.h1)
print(soup.h1.string)

# 직접 접근 방법
#<a> 태그 접근
print(soup.a) # <a> 태그 전체를 추출
print(soup.a.string) # <a> 태그 내부의 텍스트 추출 (google)
print(soup.a['href']) # <a> 태그ㅋ 내부의 href 속성의 url을 추출
print(soup.a.get('href')) # a['href'] 와 동일 기능
print(soup.a['class']) # list 타입으로 변환



# find() 함수

print(soup.find('div'))
 
print(soup.find('div',{'id':'text_id2'}))

# 여러 <div> 태그 중 특정 속성을 가지는 항목 추출
div_text = soup.find('div',{'id':'text_id2'})
print(div_text.text)

#'\n Example page\n' 
print(div_text.string)  


