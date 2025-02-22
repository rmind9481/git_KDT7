# 21 문자열 인덱싱

letters = "Python"

print(f"{letters[0],letters[2]}")


# 22 문자열 슬라이싱
# 자동차 번호가 다음과 같을때 뒤에 4자리만 출력하세요.

license_plate ="24가 2210"

print(license_plate[4:])


# 23 문자열 인덱싱

string = "홀짝홀짝홀짝"
#print(string[0],string[2],string[4])
print(string[::2])

# 24 문자열 슬라이싱

string = "PYTHON"

print("".join(reversed(string)))

# 25 문자열 치환

phone_number = "010-1111-2222"

print(phone_number.replace("-"," "))

# 26 문자열 다루기

phone_number = "010-1111-2222"

print(phone_number.replace("-",""))


# 27 문자열다루기기
url = "http://sharebook.kr"

print(url[url.index(".")+1:])


# 28 문자열은 immutable

lang = 'python'
# lang[0] = "p" 수정할수 없다.
print(lang)


# 29 replace 메서드
string = 'abcdfe2a354a32a'

string = string.replace('a','A')
print(string)


# 30 replac 메서드 
string = 'abcd'
string.replace('b', 'B')
print(string)

# 변환 없이 abcd 왜냐하면 값을 저장하지 않아서