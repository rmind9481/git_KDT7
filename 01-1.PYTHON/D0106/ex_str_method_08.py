# -----------------------------------------------------
#      str 타입 전용 함수 즉, 메서드(Method)
#   -  사용법 : 변수명.메서드명()
# -----------------------------------------------------


# [8] 문자열을 특정 조건에 맞게 변경해주는 메서드
#  => 대문자로 변경 upper()
#  => 소문자로 변경 lower()
#  => 첫글자만 대문자 나머지는 소문자 변경 capitalize()

data = 'good luck'

print(f'{data} upper() : {data.upper()}')

# 모두 대문자 변경 후 저장
data = data.upper()

print(f'{data}')


# 모두 소문자 변경 후 저장

data = data.lower();
print(f'{data}')

# 첫글자만 대문자, 나머지는 소문자로 변경 후 저장
data = data.capitalize()
print(f"{data}")