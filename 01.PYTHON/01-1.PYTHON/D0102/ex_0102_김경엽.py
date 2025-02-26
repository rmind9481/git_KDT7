# ---------------------------------------------------------------------
# [문제1] 정수 2개 입력 받은 후
#
#  7가지 산술 연산 결과를 출력
#   -출력 형태
#   9 + 3 = 12  2진수 8진수 16진수 결과로 출력
# ------------------------------------------------------------------------
# -입력 받기 : input(입력받고 데이터 요청 문자열)
#               키보드에서 입력 받음
#               입력 받은 데이테는 str 타입임


# = str 타입 => int 타입 형변환하기
num1 = int(input("1 .숫자를 입력해주세요 : "))
num2 = int(input("2 .숫자를 입력해주세요 : "))


print(" ############## 10진수 산술연산자 ##################")
print(f"더하기 {num1}+{num2} = {num1+num2}")
print(f"빼기   {num1}-{num2} = {num1-num2}")
print(f"곱하기 {num1}*{num2} = {num1*num2}")
print(f"나누기 {num1}/{num2} = {num1/num2}")
print(f"나머지 {num1}//{num2} = {num1//num2}")
print(f"몫     {num1}%{num2}  = {num1%num2}")
print(f"제곱근 {num1}**{num2} = {num1**num2}")




print(" ############## 2진수 산술연산자 ##################")
print(f"더하기 {num1}+{num2} 의 2진수 결과 값 : {bin(num1+num2)}")
print(f"빼기   {num1}-{num2} 의 2진수 결과 값 : {bin(num1-num2)}")
print(f"곱하기 {num1}*{num2} 의 2진수 결과 값 : {bin(num1*num2)}")
print(f"나누기 {num1}/{num2} 의 2진수 결과 값 : {bin(int(num1/num2))}")
print(f"나머지 {num1}//{num2} 의 2진수 결과 값 : {bin(num1//num2)}")
print(f"몫     {num1}%{num2}  의 2진수 결과 값 : {bin(num1%num2)}")
print(f"제곱근 {num1}**{num2} 의 2진수 결과 값 : {bin(num1**num2)}")

print(" ############## 8진수 산술연산자 ##################")
print(f"더하기 {num1}+{num2} 의 8진수 결과 값 : {oct(num1+num2)}")
print(f"빼기   {num1}-{num2} 의 8진수 결과 값 : {oct(num1-num2)}")
print(f"곱하기 {num1}*{num2} 의 8진수 결과 값 : {oct(num1*num2)}")
print(f"나누기 {num1}/{num2} 의 8진수 결과 값 : {oct(int(num1/num2))}")
print(f"나머지 {num1}//{num2} 의 8진수 결과 값 : {oct(num1//num2)}")
print(f"몫     {num1}%{num2}  의 8진수 결과 값 : {oct(num1%num2)}")
print(f"제곱근 {num1}**{num2} 의 8진수 결과 값 : {oct(num1**num2)}")


print(" ############## 16진수 산술연산자 ##################")
print(f"더하기 {num1}+{num2} 의 16진수 결과 값 : {hex(num1+num2)}")
print(f"빼기   {num1}-{num2} 의 16진수 결과 값 : {hex(num1-num2)}")
print(f"곱하기 {num1}*{num2} 의 16진수 결과 값 : {hex(num1*num2)}")
print(f"나누기 {num1}/{num2} 의 16진수 결과 값 : {hex(int(num1/num2))}")
print(f"나머지 {num1}//{num2} 의 16진수 결과 값 : {hex(num1//num2)}")
print(f"몫     {num1}%{num2}  의 16진수 결과 값 : {hex(num1%num2)}")
print(f"제곱근 {num1}**{num2} 의 16진수 결과 값 : {hex(num1**num2)}")



# --------------------------------------------------------------------
# [문제2] 3개 단어 입력 받은 후
#        큰 단어, 작은 단어 출력
#       -출력 형태
#       'ab' , ' abc , 'aba' => 큰 문자열 'abc'
# --------------------------------------------------------------------

str1, str2, str3 = input("단어 3개를 입력해주세요").split()

# str1 = 'ab'
# str2 = 'abc'
# str3 = 'aba'

print(f"{str1},{str2},{str3} 의 큰 문자열은 : {max(str1,str2,str3)}")
print(f"{str1},{str2},{str3} 의 작은 문자열은 : {min(str1,str2,str3)}")