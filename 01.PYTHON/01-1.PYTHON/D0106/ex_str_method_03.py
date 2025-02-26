# -----------------------------------------------------
#      str 타입 전용 함수 즉, 메서드(Method)
#   -  사용법 : 변수명.메서드명()
# -----------------------------------------------------

# [1] 문자열에서 원소의 인덱스 찾아주는 메서드 => rindex(), rfind()
#      결과값 : 0이상의 인덱스 , 없는 경우 not found ERROR 발생
data = "Happy 2025!"


print(f'p의 인덱스 : {data.rindex("p")}, {data.rfind("p")}')

last = data.rindex("p")

print(f'p의 인덱스 : {data.rindex("p",0,last)}, {data.rfind("p")}')


