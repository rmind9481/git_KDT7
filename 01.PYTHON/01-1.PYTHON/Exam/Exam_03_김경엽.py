# 문제 1 [변수] 데이터를 저장하는 코드를 작성해주세요.

# 1. 자신의 고향 도시를 저장하세요.

home = "대구"

# 2. 자신의 혈액형을 저장하세요.

boold = "B"

# 3. 좋아하는 계절을 저장하세요.

season ="winter"

# 4.키를 저장하세요

height = 200

# 5. 전화번호를 저장하세요

phone_number = "010-1234-1234"

# 6. 파이 값을 저장하세요

pi_num = 3.14

# 7. 국적을 저장하세요

Nationality = "korea"


# 문제2  알고 싶은 구구단을 입력 받은 후 구구단을 출력하세요.


num = int(input("알고 싶은 구구단 의 숫자를 입력 해주세여. :"))

print(f"{num} * {1} = {num*1}")
print(f"{num} * {2} = {num*2}")
print(f"{num} * {3} = {num*3}")
print(f"{num} * {4} = {num*4}")
print(f"{num} * {5} = {num*5}")
print(f"{num} * {6} = {num*6}")
print(f"{num} * {7} = {num*7}")
print(f"{num} * {8} = {num*8}")
print(f"{num} * {9} = {num*9}")


# 문제3 [자료형 변환] 아래 조건에 맞도록 코드를 작성하세요.

# 1. 정수 31 => 실수로 일시적 변환

num1 = 31

print(f"{num1} 실수로 일시적 변환 {float(num1)} 타입 {type(num1)}")

# 2. 정수 31 => 실수로 완전히 변환

num1 = float(num1)
print(f"{num1} 실수로 완전히 변환 {(num1)} 타입 {type(num1)}")

# 3. 정수 2022 => 문자열로 일시적 변환

msg = 2022

print(f"{msg} 문자열로 일시적 변환 {str(msg)} 타입 {type(msg)}")



# 4. 정수 2022 => 문자열로 완전히 변환

msg = str(msg)
print(f"{msg} 문자열로 일시적 변환 {str(msg)} 타입 {type(msg)}")


# 5. 실수 98.1 => 정수로 일시적 변환 

num2 = 98.1
print(f"{num2} 정수로 일시적 변환 {int(num2)} 타입 {type(num2)}")


# 6. 실수 98.1 => 정수로 완전히 변환

num2 = int(num2)
print(f"{num2} 정수로 완전히 변환 {(num2)} 타입 {type(num2)}")

# 7. 실수 98.1 => 문자열로 일시적 변환

print(f"{num2} 문자열로 일시적 변환 {str(num2)} 타입 {type(num2)}")


# 8. 실수 98.1 => 문자열로 완전히 변환

num2 = str(num2)
print(f"{num2} 문자열로 완전히 변환 {(num2)} 타입 {type(num2)}")


# 문제4 아래 조건을 만족하는 코드를 작성하세요.

# 1. 주민등록번호는 881220-1068234 입니다
# 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분을 나누어 출력하세요.

jumin = "881220-0168234"

print(f"{jumin} 입니다, \n앞부분은 { jumin[:6]}\n뒷부분은{jumin[7:]}")


# 2. 문자열 a:b:c:d 가 있습니다.
# 해당 문자열에서 a,b,c,d 만 출력하세요


msg = "a:b:c:d"

print(f"{msg[0],msg[2],msg[4],msg[6]}")



# 3. 에어컨이 월 48581원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다" 에서 총 금액을 출력해주세요.

#[출력]
# 에어컨 금액, 0,0000000

credit_card = int(input("에어컨의 36개월 할부 가격은? "))

air_conditioner = credit_card*36


print(f"에어컨 금액은 {air_conditioner} 원 입니다.")


# 4. "가로 10cm 세로 11cm 인 직사각형 넓이 계산" 문자열로 구한 값으로 직사각형 넓이 계산후 출력하세요.

# [출력] 직사각형 넓이 : 가로 10 X 세로 11 = 110


msg = "가로 10cm, 세로 11cm 인 직사각형 넓이 계산"

num1 =int(msg[3:5])
num2 =int(msg[12:14])

print(f"직사각형 넓이 : 가로 {num1} X 세로 {num2} = {num1*num2}")




# 문제5 아래 조건을 만족하는 코드를 작성하세요.


#1. 파일의 경로를 출력하는 코드
#경로 : "C:\Users\Public\kyobo\eLibrary\B2C\edir.info"


path = 'C:\\Users\\Public\\kyobo\\eLibrary\\B2C\\edir.info'

print(path)


#2. 데이터에서 가장 큰 값, 가장 작은 값, 절대값 출력 코드
#[데이터]
# 99, -5, 100, 0, 72

data1 = 99
data2 = -5
data3 = 100
data4 = 0

print(f"가장 큰값 : {max(data1,data2,data3,data4)}")
print(f"가장 작은값 : {min(data1,data2,data3,data4)}")
print(f"절대값 : {(data1,abs(data2),data3,data4)}")



# 3. 데이터를 출력하는 코드

#  오늘은 2025년 1월 1일 새해입니다.
#  문자열 데이커는 "" 사용
#  [출력] 오늘은 "2025년 1월 1일 " 새해 입니다

msg_data = "오늘은 2025년 1월 1일 새해 입니다."

msg_data2 = msg_data[:4]+"\"" + msg_data[4:15]+"\""+msg_data[15:]

print(msg_data2)


# 4. 데이터를 출력하는 코드 작성

# [데이터] 하늘과 바람과 별과 시 서시(序詩) 윤동주
# 죽는 날까지 하늘을 우러러 한 점 부끄럼이 없기를, 잎새에 이는 바람에도 나는 
# 괴로워했다. 별을 노래하는 마음으로 모든 죽어가는 것을 사랑해야지 그리고 
# 나한테 주어진 길을 걸어가야겠다. 오늘 밤에도 별이 바람에 스치운다.


print(f"하늘과 바람과 별과 시\n\n\t서시(序詩)\n\t\t\t윤동주\n\n\
죽는 날까지 하늘을 우러러\n한 점 부끄럼이 없기를,\n잎새에 이는 바람에도\n나는\
괴로워했다.\n\n별을 노래하는 마음으로\n모든 죽어가는 것을 사랑해야지\n그리고\
나한테 주어진 길을\n걸어가야겠다.\n\n오늘 밤에도 별이 바람에 스치운다.")