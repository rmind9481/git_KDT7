# -----------------------------------------------------------
#   [문] 나무 + 메세지 출력
# -----------------------------------------------------------


print(" "*7+"*")
print(" "*6+"*"*3)
print(" "*5+"*"*5)
print(" "*4+"*"*7)
print(" "*3+"*"*9)
print(" "*2+"*"*11)
print(" "*1+"*"*13)
print(" "*0+"*"*15)
print(" "*6+"*"*4)
print(" "*6+"*"*4)
print(" "*6+"*"*4)
print("Merry Christmas".center(15))
print("2025".center(15))



# -----------------------------------------------------------
#   [문] 숫자 2개를 입력 받은 후 산술 연산 수행 후 출력해 주세요.
#           덧셈 뺄셈 곱셈 나눗셈
#   -input() 내장함수 => str 
#   -str => int 형변환
# -----------------------------------------------------------

# (1) 숫자 2개 입력 받기
n1 = (input("숫자 1개 입력").strip())
n2 = (input("숫자 1개 입력").strip())

# (2) 덧셈, 뺄셈,곱셈. 나눗셈 
# -str => int 형변환
# - 검사 : 빈칸 여부, 0~9만 존재

print(f"n1 요소 갯수 : {len(n1)}개 숫자 문자열 여부 : {n1.isdecimal()}")
print(f"n2 요소 갯수 : {len(n2)}개 숫자 문자열 여부 : {n1.isdecimal()}")

# (3) - 숫자 문자열 여부
print(f"n1의 숫자 문자열 여부 : {n1[1:].isdecimal()}")

print(f"덧셈 {n1} + {n2} = {n1+n2}입니다")
print(f"뺄셈 {n1} - {n2} = {n1-n2} 입니다")
print(f"곱셈 {n1} * {n2}  = {n1*n2}입니다")
print(f"나눗셈 {n1} / {n2} = {n1/n2} 입니다")



# - 숫자 문자열 여부 (실수) => . 위치가 유동적
f1 = n1.replace('.','')

print(f"n1의 숫자 문자열 여부 : {f1.isdecimal()}")



# [문] data = "Hello" 에서 olleH 로 출력하세요

data = "Hello"
print(f"{data[::-1]}")