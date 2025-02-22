# -------------------------------------------------------------------
# str 타입의 연산자 - 맴버 연산자
# - 문법 왼쪽 in 오른쪽 
# - 기능 : 왼쪽 데이터가 오른쪽에 존재하는 요소/원소
#           여부를 판단함 ===> 결과 : True/False
# -------------------------------------------------------------------

# in 연산자 : 오른쪽에 존재하면 True
print(f"'P' in 'Price is 10000' : {'P' in 'Price is 10000' }")
print(f"' p' in 'Price is 10000' : {'p' in 'Price is 10000' }")
print(f"' P' in 'Price is 10000' : {' p' in 'Price is 10000' }")
print(f"'1' in '12345' => {'1' in '12345'}")
print(f"'7' in '12345' => {'1' in '12345'}")
print(f"'11' in '12345' => {'11' in '12345'}")



# not in 연산자 : 오른쪽에 존재하지 않으면 True
print(f"'P' not in 'Price is 10000' : {'P' not in 'Price is 10000' }")
print(f"' p' not in 'Price is 10000' : {'p' not in 'Price is 10000' }")
print(f"' P' not in 'Price is 10000' : {' p' not in 'Price is 10000' }")
print(f"'1' not in '12345' => {'1' not in '12345'}")
print(f"'7' not in '12345' => {'1' not in '12345'}")
print(f"11 not in '12345' => {'11' not in '12345'}")


# [실습] 주민번호 7번째 자리의 숫자를 확인해서 남자 인지 여부 출력

# - 남자 : 1,3,5,7
# - 여자 : 2,4,6,8
jumin = '111111-3000000'


print(f"남자? : {jumin[7] =='1' or jumin[7] =='3' or jumin[7] =='5' or jumin[7] =='7' } ")

print(f"남자 ? : {jumin[7] in '1357'} ")

