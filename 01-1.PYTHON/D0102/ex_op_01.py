# ---------------------------------------------------------
# 연산자 (Operator) - 산술연산자
#   - 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/)
#   - 몫(//), 나머지(%), 제곱근(**)
# ---------------------------------------------------------


# int, float 타입의 산술연산 ---------------------------------------

# num1 = 7.5
# num2 = 5.25

# print(f'{num1}+{num2} = {num1 + num2}')
# print(f'{num1}-{num2} = {num1 - num2}')
# print(f'{num1}*{num2} = {num1 * num2}')
# print(f'{num1}/{num2} = {num1 / num2}')
# print(f'몫 {num1}//{num2} = {num1 // num2}')
# print(f'나머지 {num1}//{num2} = {num1 % num2}')
# print(f'제곱근 {num1}**{num2} = {num1 ** num2}')

# str 타입의 산술연산 ------------------------------------------------

# str1 = 'a'
# str2 = 'b'

# print(f'덧셈 -문자열 연결 : str + str {str1}+{str2} = {str1 + str2}')
# print(f'곱셉 -문자열 정수n만큼 반복 : str * 정수 {str1}*3 = {str1 * 3}')

# #  에러 TypeError: unsupported operand type(s) for -: 'str' and 'str'
# #  - 연산자는 문자 타입에서 미지원 print(f'{str1}-{str2} = {str1 - str2}')

# #  에러 can't multiply sequence by non-int of type 'str'
# #  타입 문자 * 정수
# # print(f'{str1}*{str2} = {str1 * str2}')


# # 에러 TypeError: unsupported operand type(s) for /: 'str' and 'str'
# # 미지원 
# # print(f'{str1}/{str2} = {str1 / str2}')
# # print(f'몫 {str1}//{str2} = {str1 // str2}')
# # print(f'나머지 {str1}//{str2} = {str1 % str2}')
# # print(f'제곱근 {str1}**{str2} = {str1 ** str2}')


# # 실습

# print("Happy" + "New" + "Year" + "2025") 

# print("Lucky" * 7)







# bool 타입의 산술연산 ----------------------------------------


# int, float 타입의 산술연산 ---------------------------------------
# 0 -- False , 1 -- True
num1 = False
num2 = True

print(f'{num1}+{num2} = {num1 + num2}')
print(f'{num1}-{num2} = {num1 - num2}')
print(f'{num1}*{num2} = {num1 * num2}')
print(f'{num1}/{num2} = {num1 / num2}')
print(f'몫 {num1}//{num2} = {num1 // num2}')
print(f'나머지 {num1}%{num2} = {num1 % num2}')
print(f'제곱근 {num1}**{num2} = {num1 ** num2}')