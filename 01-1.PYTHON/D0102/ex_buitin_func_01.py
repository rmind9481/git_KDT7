# -------------------------------------------------------
# 내장 함수 - 수치데이터 관련 내장함수들
# -------------------------------------------------------

# [1] 절대값 변환 내장함수 abs()

print(f"-5 절대값 : {abs(-5)}")
print(f"-5.5 절대값 : {abs(-5)}")


# [2] 큰 값 반환 함수 내장함수 max()


print(f"max(-5,10) : {max(-5,10)}")
print(f"max(-5,10,2025) : {max(-5,10,2025)}")

# => 코드값 변환 후 비교해서 큰 값 찾아줌
print(f"max('a','b','c') : {max('a','b','c')}")
print(f"max('abx','bxb','cxa') : {max('abx','bxb','cxa')}")


# [3] 작은 값 반환 함수 내장함수 min()


print(f"min(-5,10) : {min(-5,10)}")
print(f"min(-5,10,2025) : {min(-5,10,2025)}")


# => 코드값 변환 후 비교해서 작은 값값 찾아줌
print(f"min('a','b','c') : {min('a','b','c')}")
print(f"min('abx','bxb','cxa') : {min('abx','bxb','cxa')}")


# [4] 거듭제곱 계산 내장함수 pow(a,b)
print(f"2의 3승 : {pow(2,3)}")
print(f"2의 5승 : {pow(2,5)}")
print(f"2의 -5승 : {pow(2,-5)}")


# [5] 실수 반올림 내장함수 round(a, 자릿수)
num = 5.1256290

print(f'{num} 의 소수점 이하 0자리: {round(num,0)}')
print(f'{num} 의 소수점 이하 1자리: {round(num,1)}')
print(f'{num} 의 소수점 이하 2자리: {round(num,2)}')
print(f'{num} 의 소수점 이하 3자리: {round(num,3)}')
print(f'{num} 의 소수점 이하 4자리: {round(num,4)}')
print(f'{num} 의 소수점 이하 5자리: {round(num,5)}')
print(f'{num} 의 소수점 이하 6자리: {round(num,6)}')

