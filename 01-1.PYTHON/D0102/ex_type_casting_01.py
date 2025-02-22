# ----------------------------------------------------------------------
# 데이터 타입/종류 를 변경해주는 내장함수
# - 타입 캐스팅(Casting) / 형변환
# * 데이터 타입/종류를 변경하는것
# * 종류 - 암묵적 형변환 : 시스템에서 진행
#        - 명시적 형변환 : 개발자가 진행
# * 함수 - 자료형명()
# * 예시 - int(), float(), bool(), str()
# ----------------------------------------------------------------------


# [1] 정수 int 타입으로 형변환하기 => int(데이터)
# float => int 변환 : 데이터 손실 발생 가능함

print(f"5.12 => int 로 형변환 :{int(5.12)}")
print(f"5.99 => int 로 형변환 :{int(5.99)}")

# str => int 변환 : 10진수 숫자 즉, 0~9만 음수(-) 기호 가능
print(f" '32' => int 로 형변환 : {int('32')} {type(int('32'))}" )
# print(f" '32.' => int fh gudqusghks : {int('32.')} {type(int('32.'))}" )
print(f" '-32' => int 로 형변환 : {int('-32')} {type(int('-32'))}" )

# bool => int 변환 : 10진수 숫자 즉, 0~9만 가능
print(f"True => int 로 형변환 :{int(True)} {type(int(True))}")
print(f"False => int 로 형변환 :{int(False)} {type(int(False))}")


# str => int 변환 : 2진수 0b 8진수 0o 16진수 0x
# 28 => 0b11100, 0o34, 0x1c

print(f"'0b11100' => int로 형변환 : {int('0b11100',base=2)} {type(int('0b11100',base=2))}")
print(f"'0o34' => int로 형변환 : {int('0o34',base=8)} {type(int('0o34',base=8))}")
print(f"'0x1c' => int로 형변환 : {int('0x1c',base=16)} {type(int('0x1c',base=16))}")



