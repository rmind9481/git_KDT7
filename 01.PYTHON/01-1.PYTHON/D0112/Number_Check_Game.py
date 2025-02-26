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
    print(f"종료버튼 : X")
    n1 = (input("\n숫자를 입력해주세요 :").strip())
    

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
    elif n1 in ['x',"X"]:
        print(f'종료합니다.')
        break

    else:
        print(f'잘못된 값입니다. 다시 입력해주세요')