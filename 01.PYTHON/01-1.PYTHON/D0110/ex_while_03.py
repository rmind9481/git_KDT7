# ------------------------------------------------------------------
#   제어문 - while 반복문
#   - 반복 횟수가 미정인 경우에도 사용 가능함
#   - 반복 횟수가 정해진 경우에도 사용 가능함
# ------------------------------------------------------------------


import random 
import math

# 수학 에 pi 의 값 불러오기
print(math.pi)

# 랜덤 인스턴스/객체 생성 => 힙영역 저장
r = random.Random() 



# 랜덤 인스턴스/ 객체가 가진 기능 즉, 메서드 사용

# random() 메서드 : 0.0 <= ~ < 1.0 범위에서 숫자 1개 추출

for i in range(10):
    value = r.random()
    print(r.random())
    print(value, int(value), int(value*10))

# randint(a,b) : a <= ~ <= b 범위에서 정수 1개 추출

for i in range(10):
    value = r.randint(1,10)
   
    print(value)
# -------------------------- 
# 리스트를 사용해서 랜덤
lotto = []

while True :
    # 1 ~ 45 사이의 임의의 숫자 추출 및 중복 검사 후 저장
    num = r.randint(1,45)
    if num not in lotto : # 로또 리스트안에 숫자가 없어면 추가
        lotto.append(num)   
    
    if len(lotto) == 6 :
        print(f"오늘의 로또번호 : {lotto}")
        break;
# -------------------------- 
# set 사용해서 랜덤
lotto2 = set()

while True :
    # 1 ~ 45 사이의 임의의 숫자 추출 및 중복 검사 후 저장
    num = r.randint(1,45)
    
    lotto2.add(num)

    if len(lotto2) == 6 :
        print(f"오늘의 로또번호 : {lotto2}")
        break;


# 로또 번호 생성기

num = []
for i in range(6):

    while len(num) < 6:
        num.append(random.randint(1,45))
        num = set(num)
        num = list(num)

print(num)

# --------------------------


# 임의의 숫자 설정 

myLuck_number = random.randint(1,100)

print(f" 1~100 까지 빙고 게임~~")
while True:
    
    num = input("숫자를 입력해주세요:")
    if len(num) > 0 and num.isnumeric:
        num = int(num)
        if num == (myLuck_number) :
            print(f"{num} @@ 빙고~~ @@ \n정답입니다.")
            break;
        elif num > (myLuck_number) :
            print(f"입력하신 숫자가 큽니다. Down")
            
        elif num < (myLuck_number) :
            print(f"입력하신 숫자가 적습니다. Up") 
    else:
        print(f"{num} 잘못된 값 다시 입력해주세요")