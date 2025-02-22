# -----------------------------------------------------
#      str 타입 전용 함수 즉, 메서드(Method)
#   -  사용법 : 변수명.메서드명()
# -----------------------------------------------------

# [1] 문자열에서 원소의 인덱스 찾아주는 메서드 => index() , find()
#      결과값 : 0이상의 인덱스 , 없는 경우 not found ERROR 발생
data = "Happy 2025!"


# - 'y'원소의 인덱스 찾기

print(f"y의 인덱스 : {data.index('y')}")

# - '5'원소의 인덱스 찾기
print(f"y의 인덱스 : {data.index('5')}")


# - '25'원소의 인덱스 찾기
print(f"25의 인덱스 : {data.index('25')}")


# - '  '원소의 인덱스 찾기 => 엾는 경우 not found ERROR
# print(f"' '의 인덱스 : {data.index(' ')}")

# ValueError: substring not found 에러 인덱스 없는 경우



# [2] 문자열에서 원소의 인덱스 찾아주는 메서드 => find()
#      결과값 : 0이상의 인덱스 , 없는 경우 -1 not found ERROR 발생


# - 'y'원소의 인덱스 찾기

print(f"y의 인덱스 : {data.find('y')}")

# - '5'원소의 인덱스 찾기
print(f"y의 인덱스 : {data.find('5')}")


# - '25'원소의 인덱스 찾기
print(f"25의 인덱스 : {data.find('25')}")

# - ' '원소의 인덱스 찾기 
print(f"' '의 인덱스 : {data.find(' ')}")

# - '  '원소의 인덱스 찾기 => 없는 경우 -1 반환
print(f"'  '의 인덱스 : {data.find('  ')}")

# ==> 'p' 인덱스 찾기 : 0번 원소부터 찾기

print(f'p의 인덱스 : {data.index("p")}, {data.find("p")}')



# => 2번째 "p" 인덱스 찾기 : 지정된원소부터 찾기

frist = data.index('p')
print(f'p의 인덱스 : {data.index("p",frist+1)}, {data.find("p",frist+1)}')



# 여러개의 동일 문자 인덱스 찾기
data = "Good Good Good"

# => "G" 인덱스 찾기

idx = data.find('G')
print(f"첫번째 G 인덱스 : {idx}번째 원소")

idx = data.find("G", idx+1)
print(f"두번째 G 인덱스 : {idx}번째 원소")

idx = data.find("G", idx+2)
print(f"세세번째 G 인덱스 : {idx}번째 원소")

idx = data.find("G", idx+1, 11) # idx+1 <= ~ <11
print(f"세세번째 G 인덱스 : {idx}번째 원소")