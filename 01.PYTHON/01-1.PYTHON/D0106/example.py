# [문제1]
# "에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있씁니다." 금액을 출력해주세요.


# 인덱싱이랑 슬라이싱을 사용

msg = "에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다."

# - 전체 원소 갯수 확이
print(f"msg 의 원소 갯수 : {len(msg)}개")



# - 월 금액만 추출 => 7 ~ 12

month = msg[7:13]
print(f"월 금액 : {month}원")


# - 월 금액에서 "," 제거 => month = 48,584

month = month[:2] + month[3:]

print(f"월 금액 : {month}원")

# - 개월 수 추출 : 20,21

count = msg[20:22]
print(f"할부 개월수: {count}")


# - 금액 계산 => str 타입을 int타입으로 형 변환

total = int(month)*int(count)

total = str(total)

print(f"총 금액 : {total} ")

# [출력] 에어컨 금액 : 0,000,000원

total= total[0]+","+total[1:4]+","+total[4:]

print(f"총 금액 : {total} ")


# [문제2] "가로 10cm, 세로 11cm인 직사각형 넓이 계산"

data = "가로 10cm, 세로 11cm 인 직사각형 넓이 계산"


print(f"data의 원소 갯수 : {len(data)}개")

# -가로 길이 숫자 => 인덱스 3번 4번

width = data[3:5]
print(f"가로 길이 :{width}")

# -세로 길이 숫자 => 인덱스 12번 15번
height = data[12:14]

print(f"세로 길이 : {height}")

result = int(width)*int(height)

# [출력] 직사각형 넓이 : 가로 10 X 세로 11 = 110

print(f"직사각형 넓이 : 가로 {width} X 세로{height} = {result}")





# [문제3] 문자를 입력 받아 문자의 코드값과 코그값을 기계어로 출력하세요


data = input("문자 1개 입력 :")
code = ord(data)
bvalue = bin(code)

print(f"{data} 코드값 : {code}  {data} 기예어 : {bvalue}")
print(f"{data} 코드값 : {code}  {data} 기예어 : {bvalue[2:]}")