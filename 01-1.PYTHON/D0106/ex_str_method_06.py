# -----------------------------------------------------
#      str 타입 전용 함수 즉, 메서드(Method)
#   -  사용법 : 변수명.메서드명()
# -----------------------------------------------------


# [6] 문자열을 구성하는 문자의 종류 즉, 숫자, 알파벳, 기호 문자.........
#   검사 해주는 메서드 => isdigit(),.... => 결과: True/False
#                        isdigit(),isdecimal(),isnumeric() => 결과: True/False
#   숫자 표현형태 포함 범위 => isdecimal() < isdigit() 제곱근 < isnumberic() 제곤급, 분수
data1 = '0123456789'
data2 = '010-1111-2222'
data3 = '0.00001'
data4 = '2²'
data5 = "⅔" 
data6 = "-58"


# -> 숫자로 구성된 str인지 체크 : isdigit() 0~9만 가능함!
print(f'{data1} data1.isdecimal() => {data1.isdecimal()}')
print(f'{data1} data1.isdigit() => {data1.isdigit()}')
print(f'{data1} data1.isnumeric() => {data1.isnumeric()}\n')


print(f'{data2} data1.isdecimal() => {data2.isdecimal()}')
print(f'{data2} data1.isdigit() => {data2.isdigit()}')
print(f'{data2} data1.isnumeric() => {data2.isnumeric()}\n')

print(f'{data3} data1.isdecimal() => {data3.isdecimal()}')
print(f'{data3} data1.isdigit() => {data3.isdigit()}')
print(f'{data3} data1.isnumeric() => {data3.isnumeric()}\n')

print(f'{data4} data1.isdecimal() => {data4.isdecimal()}')
print(f'{data4} data1.isdigit() => {data4.isdigit()}')
print(f'{data4} data1.isnumeric() => {data4.isnumeric()}\n')

print(f'{data5} data1.isdecimal() => {data5.isdecimal()}')
print(f'{data5} data1.isdigit() => {data5.isdigit()}')
print(f'{data5} data1.isnumeric() => {data5.isnumeric()}\n')

print(f'{data2} => {data2.isdigit()}')
print(f'{data3} => {data3.isdigit()}')



# 숫자 체크하는 메서드 
print(f"{data1} => {data1.isnumeric()}")
print(f"{data1} => {data1.isdecimal()}")




# -> 문자(사람이 사용하는 언어) 즉, 알파벳, 자음모음으로 구성된 str인지 체크
# -> 기호(?,!,#) 문자 안됨
# isalpha()

data1="Happy"
data2="월요일"
data3="地獄の門を開けましたか"
data4="今天"
data5="今天0106"

print(f"{data1} => {data1.isalpha()}")
print(f"{data2} => {data2.isalpha()}")
print(f"{data3} => {data3.isalpha()}")
print(f"{data4} => {data4.isalpha()}")
print(f"{data5} => {data5.isalpha()}")



# -> 문자와 숫자만으로 구성되어 있는지 여부 : isalnum()
# -> 기호(?,!,#) 문자 안됨

data1 = "Happy2025"
data2 = "happy 2025"

print(f"{data1} => {data1.isalnum()}")
print(f"{data2} => {data2.isalnum()}")