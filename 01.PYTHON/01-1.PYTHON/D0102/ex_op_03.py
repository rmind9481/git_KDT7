# -------------------------------------------------------------------
# 연산자 (Operator) - 논리 연산자자
#   - 왼쪽 and 오른쪽 : 그리고
#       True and True => True
#       True and False => False
#       False and True => Falsee
#       False and False => True
#       
#   - 왼쪽  or 오른쪽 : 또는
#       True or True => True
#       True or False => True
#       False or True => True
#       False or False => False
#
#   - not 오른쪽 : 오른쪽 반대 / 토글(Toggle)
#       not True => False
#       not False => True
# -------------------------------------------------------------------


# 20대 남자인 경우 => 나이 와 성별 모두 맞아야함
gender = '남자'
age = 32
#print(gender == '남자'  and   30 > age >= 20)

# 20대 나이 체크

# print(f'{age} 는? {30 > age >= 20}')
# print(f'{age} 는? {30 > age and age >= 20}')


# - 20대 나이와 성별 체크
print(f"{age}, {gender} 는 ? {(age>=20 and age < 30) and gender == '남자'}")

print( "20대 이상",age >=20 )
print( "20대 ", 30 > age >=20 )
print( "30대 이상 또는 여자 ", age >=30 or gender != '남자')


# not 연산자 : 현재 결과를 반대로 -----------------------------------------------

print(f"{age} >= 20 : {age>=20}")
print(f"not {age} >= 20 : {not age>=20}")

# -> not True/False
# -> int/ Float => 0 또는 0.0 : False, 나머지 숫자 : True
print(f'not 1 : {not 1}')
print(f'not 0 : {not 0}')
print(f'not -1 : {not -1}')