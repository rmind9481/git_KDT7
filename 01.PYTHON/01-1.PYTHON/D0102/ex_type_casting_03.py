# ----------------------------------------------------------------------
# 데이터 타입/종류 를 변경해주는 내장함수
# - 타입 캐스팅(Casting) / 형변환
# * 데이터 타입/종류를 변경하는것
# * 종류 - 암묵적 형변환 : 시스템에서 진행
#        - 명시적 형변환 : 개발자가 진행
# * 함수 - 자료형명()
# * 예시 - int(), float(), bool(), str()
# ----------------------------------------------------------------------

# [3] 논리 bool 타입으로 형변환 하기 => bool(데이터)
# int => bool 형 변환 : 0 = false , 나머지 숫자 = True

print(f' -8 을 float 형 변환 : {bool(-8)}')
print(f' 7 을 float 형 변환 : {bool(7)}')
print(f' 0 을 float 형 변환 : {bool(0)}')




# str ==> bool 형변환 : '', "" 아무것도 없으면 False , 나머지 True
# '',"" : empty string 빈문자열
# ' '," " : whitespace string 공백문자열
 
print(f" 'a' 을 bool 형 변환 : {bool('a')}")
print(f" 'abc' 을 bool 형 변환 : {bool('abc')}")
print(f" '' 을 bool 형 변환 : {bool('')}")
print(f" ' ' 을 bool 형 변환 : {bool(' ')}")


# float ==> bool 형 변환

print(f" 3. 을 float 형 변환 : {bool(3.)}")
print(f" -0.123 을 float 형 변환 : {bool(-0.123)}")
print(f" 0.0 을 float 형 변환 : {bool(0.0)}")