# ----------------------------------------------------------------------
# 데이터 타입/종류 를 변경해주는 내장함수
# - 타입 캐스팅(Casting) / 형변환
# * 데이터 타입/종류를 변경하는것
# * 종류 - 암묵적 형변환 : 시스템에서 진행
#        - 명시적 형변환 : 개발자가 진행
# * 함수 - 자료형명()
# * 예시 - int(), float(), bool(), str()
# ----------------------------------------------------------------------

# [2] 실수 float 타입으로 형변환 하기 => float(데이터)
# int => float 형 변환

print(f' -8 을 float 형 변환 : {float(-8)}')
print(f' 7 을 float 형 변환 : {float(7)}')




# str ==> float 형변환

print(f" '-8' 을 float 형 변환 : {float('-8')} {type(float('-8'))}")
print(f" '0.123' 을 float 형 변환 : {float('0.123')}{type(float('0.123'))}")
print(f" '0b11100' 을 float 형 변환 : {float(int('0b11100',base=2))}{type(float(int('0b11100',base=2)))}")


# bool ==> float 형변환

print(f'True 를 float 형 변환 : {float(True)}')
print(f'False 를 float 형 변환 : {float(False)}')