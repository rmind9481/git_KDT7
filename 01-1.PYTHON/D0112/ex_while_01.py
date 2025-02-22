# ---------------------------------------------------
# [문1] 'hello' 의 문자를 하나씩 화면에 출력
#  - for 반복문 과 while 반복문 사용해서 구현
#----------------------------------------------------

# -for 반복문

# msg = "hello"

# for i in msg:
#     print(i, end='')

# print()
# # - while 반복문

# n1 = 0 

# while n1 < len(msg):
#     print(msg[n1],end='')
#     n1 +=1


# -------------------------------------------------------------
# [문2] 5 단 구구단 출력
# - for 반복문 과 while 반복문 사용해서 구현
# -------------------------------------------------------------

# dan = 1

# for i in range(2,10):
#      while dan < 10 :
#         print(f'{i}*{dan}={i*dan}')
#         dan+=1

# --------------------------------------------------------------

# dataList = [['a','b','c'],['1','2'],['%','#','@']]
# #               0번 원소    1번원소     2번원소

# for data in dataList :
#     print(data)
#     for ch in data:
#         print('-> 원소', ch)

# print("END")

# oidx = 0
# while oidx < len(dataList):
#     print(dataList[oidx])
#     iidx = 0
#     while iidx < len(dataList[oidx]):
#         print(iidx, dataList[oidx][iidx])
#         iidx +=1 
#     oidx = oidx+1


# --------------------------------------------------------------------
# 반복문 중단 : break
# --------------------------------------------------------------------

# 1 ~ 50 까지 숫자 중에서 7의 배수일 경우 출력 중단

# nums = list(range(1,51))

# for num in nums:
#     if not num%7:
#         break
#     print(num)



# num = 1

# while num<51:
#     print(num)
#     num +=1


# ---------------------------------------------------------
# 사용자로 부터 숫자를 입력 받습니다.
# ---------------------------------------------------------

# while True:
#     data = input("데이터 입력").strip()

#     if data in ['x','X']:
#         print("입력중단")
#         break
# /

# ----------------------------------------------

import random


num = random.randint(1,100)

Energe = 10
Energe_w = 0

print(f"######### @@@@@@@@@@@@@@@ #############")
print(f"#########                 #############")
print(f"######### 숫자 맞추기 게임 #############")
print(f"#########                 #############")
print(f"######### @@@@@@@@@@@@@@@ #############")
    
while True : 

# 생명체크
    if Energe == 0:
            print(f" ######################")
            print(f"    실패 입니다!!!!!!")
            print(f" ######################")
            break

    print(f"\nENERG_BAR : {'■ '*Energe +'□ '*Energe_w} ")
    n1 = (input("숫자를 입력해주세요.").strip())


# 입력값이 숫자 인지 체크
    if n1.isnumeric():
# 숫자면 정수로 변환
        n1 = int(n1)

        if n1 == num :
            print(f" ######################")
            print(f"{num} 정답입니다.")
            print(f" ######################")
            break
            
        elif 1<= n1 < num:
            print(f"UP 입니다.")
            Energe -=1 
            Energe_w+=1
        elif 100 >= n1 > num:
            print(f"Down 입니다.")
            Energe -=1 
            Energe_w+=1

    else:
        print(f'잘못된 값입니다. 다시 입력해주세요')

    
    
        
