# 문제1 자료형 (데이터 타입)에 대해 간단하게 설명해주세요.

# 자료형 데이터는 
# int(실수) float(소수) 등을 사용하는 숫자형
# str (문자)  등을 사용하는 문자형
# 참/거짓 True/ False 를 사용해서 값을 전달하는 논리형
# 등이 있습니다.



# 문제2. 파이썬 자료형 종류별 예시 및 타입 출력하는 코드를 작성해주세요.


print("############### 자료형 종류별 예시 및 타입 ###################")


num1_int = 1
num2_flaot = 5.5
str_1 = "Hello"
is_date1 = True
is_date2 = False

print(f" int 형 변수 {num1_int} => {type(num1_int)}")
print(f" float 형 변수 {num2_flaot} => {type(num2_flaot)}")
print(f" str 형 변수 {str_1} => {type(str_1)}")
print(f" bool(논리) 형 변수 {is_date1} => {type(is_date1)}")
print(f" bool(논리) 형 변수 {is_date2} => {type(is_date2)}")


# 문제3. 정수 31을 2진수 8진수 10진수 16진수로 출력하세요.


num = 31

print(f"{num} 의 2진수 표현법 입니다. : {bin(num)}")
print(f"{num} 의 8진수 표현법 입니다. : {oct(num)}")
print(f"{num} 의 10진수 표현법 입니다. : {(num)}")
print(f"{num} 의 16진수 표현법 입니다. : {hex(num)}")



# 문제4. 아래 데이터를 지정하는 자료형으로 변환하세요.

# 1. average =98.7 정수로 변환 시켜주세요

average = 98.7
print(f"average = {average} 타입은 : {type(average)}")

average = int(average)
print(f"average = {average} 타입은 : {type(average)}")


# 2. year =2022 실수로 변환시켜주세요

year = 2022
print(f"year = {year} 타입은 : {type(year)}")

year = float(year)
print(f"year = {year} 타입은 : {type(year)}")


# 3. greeting ="Hello~" 논리형 변환시켜주세요

greeting ="Hello~"
print(f"greeting = {greeting} 타입은 : {type(greeting)}")

greeting = bool(greeting)
print(f"greeting = {greeting} 타입은 : {type(greeting)}")



# 문제5. 2개의 정수를 입력 받아서 산술연산 수행 결과를 출력하는 코드를 작성하세요.

num1 = int(input("1. 숫자를 입력해주세요. :"))
num2 = int(input("1. 숫자를 입력해주세요. :"))



print(f" ########### 산술 연산자 #############")
print(f" 덧 셈 {num1} + {num2} = {num1+num2}")
print(f" 뺄 셈 {num1} - {num2} = {num1-num2}")
print(f" 곱 셈 {num1} * {num2} = {num1*num2}")
print(f" 나눗셈{num1} / {num2} = {num1/num2}")
print(f" 몫    {num1}// {num2} = {num1//num2}")
print(f" 나머지{num1} % {num2} = {num1%num2}")
print(f" 제곱근{num1} ** {num2} = {num1**num2}")

# 문제6. 문자를 입력 받아 문자의 코드값과 코드값을 기계어로 출력하세요.

# [입력] 문자 1개 입력 : ?
# [출력] 코드값 :     기계어 : 


msg = input("문자 1개를 입력 해주세요 : ")

print(f"코드 값 : {ord(msg)} , 기계어 : {bin(ord(msg))}")


# [입력] 문자 1개 입력 : A
# [출력] 코드값 :     기계어 : 

msg = input("문자 1개를 입력 해주세요 : ")

print(f"코드 값 : {ord(msg)} , 기계어 : {bin(ord(msg))}")






