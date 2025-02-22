# -----------------------------------------------------
#      str 타입 전용 함수 즉, 메서드(Method)
#   -  사용법 : 변수명.메서드명()
# -----------------------------------------------------


# [7] 문자열을 구성하는 알파벳 관련 검사해주는 메서드드
#  => 대문자, 소문자, 첫글자가 대문자,..... isOOOOO()


data ="Happy"


# -모든 문자가 대문자인지 여부 : isupper()

print(f"{data} isupper() => {data.isupper()}")


# -모든 문자가 소문자인지 여부 : islower()
print(f"{data} islower() => {data.islower()}")


# -첫글자가 대문자인지 여부 나머지 소문자인지 여부 : istitle()

print(f"{data} istitle() => {data.istitle()}")

# -공백체크 여부 : isspace()
data=" "
print(f'{data} isspace() => {data.isspace()}')

data="Goood "
print(f'{data} isspace() => {data.isspace()}')


# [실습] 정수를 입력하세요. 나이를 입력하세요.
# 입력 받기
number = input("정수 입력 : ")

print( '숫자만 구성?', number.isnumeric())
print( '숫자와 알파벳만 구성?', number.isalnum())
# str => int 형변환
number = int(number)

print(f"입력 데이터 갯수 : {len(number)}")
