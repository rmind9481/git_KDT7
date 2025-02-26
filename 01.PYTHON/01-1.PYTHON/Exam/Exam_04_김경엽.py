# 1-1. "Happy New Year 2022" 문자열에서 2022를 2023으로 변경해 주세요.


msg = "Happy New Year 2022"
print(msg)

msg = msg.replace("2022","2023")

print(msg)


# 1-2. "christmas" 문자열을 모두 대문자로 변경해주세요.

msg = "christmas"

print(msg)

msg = msg.upper()

print(msg)

# 1-3. phone_number = "010-1111-2222" 문자열을 "01011112222" 로 출력해주세요.


phone_number = "010-1111-2222"

print(phone_number.replace("-",""))

# 1-4. count = "5,96,782,550" 문자열에서 콤마(,) 를 제거하고 정수로 출력


count = "5,96,782,550"
print(count)
count = count.replace(",","")
print(int(count))


# 1-5. "산토토끼 토끼야 어디를 가느냐 폴짝 폴짝 뛰면서 어디를 가느냐" 에서 "어디를"이 몇개 있는지 출력해주세요.


msg = "산토끼 토끼야 어디를 가느냐 폴짝 폴짝 뛰면서 어디를 가느냐"

print(f"{msg} 에서 '어디를' 몇번 ? {msg.count('어디를')}")

# 1-6. "1,234,567,890" 문자열을 나누어 주세요.


num_str = "1,234,567,890"

num_str = num_str.split(",")
print(num_str)


# 1-7. koko@naver.com 에서 "@"의 인덱스를 축력해 주세요.


email = "koko@naver.com"

print(f" koko@naver.com '@' 몇번째 인덱스? {email.index('@')}")



# 1-8. "          오늘은 날씨가 너무 좋군요!!  "에서 공백을 제외한 문자의 길이를 출력해 주세요.

msg = "          오늘은 날씨가 너무 좋군요!!  "

print(f"{msg} 의  문자열 길이 :{len(msg)} ")
      
msg ="".join(msg.split())

print(f"{msg} 의  문자열 길이 :{len(msg)} ")
      


# 2 아래 출력 결과가 나오도록 코드를 작성하세요.

star = "*"


print(f"{star.center(20)}")
print(f"{(star*3).center(20)}")
print(f"{(star*6).center(20)}")
print(f"{(star*9).center(20)}")
print(f"{(star*12).center(20)}")
print(f"{(star*4).center(20)}")
print(f"{(star*4).center(20)}")
print(f"Merry Chrismas".center(20))
print(f"2025".center(20))



# 3-1 숫자 2개를 입력 받은 후 산술연산 수행 후 출력해주세요.

a,b = input("숫자 2개를 ',' 입력해주세요.").split(",")

a = int(a)
b = int(b)
print(f"입력 받은 숫자는 {a} , {b} 입니다")
print(f"덧셈 {a} + {b} = {a+b}입니다")
print(f"뺄셈 {a} - {b} = {a-b} 입니다")
print(f"곱셈 {a} * {b}  = {a*b}입니다")
print(f"나눗셈 {a} / {b} = {a/b} 입니다")


# 3-2 좋아하는 단어를 입력 받은 후 대문자로 변환하여 출력하세요.
#그리고 단어 안에 'a' 알파벳이 들어 있는지 True / False 로 결과를 출력해주세요.

data = input("좋아하는 영어 단어를 입력해주세요 :")

print(f"대문자 변환 : {data.upper()}")
print(f"영어 단어 안에 'a'가 있는지 체크 : {data.find('a') != -1}")



# 3-3 "가나*마바사*자***파하"에서 첫 번째 *의 인덱스를 출력하세요.

msg = "가나*마바사*자***파하"

print(f"* 인덱스 위치 {msg.index('*')}")




# 3-4 "Hello" 를 "olleH"로 출력하세요.

msg ="Hello"
msg = ''.join(reversed(msg))
print(msg)