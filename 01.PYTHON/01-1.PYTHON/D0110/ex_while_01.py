# ------------------------------------------------------------------
#   제어문 - while 반복문
#   - 반복 횟수가 미정인 경우에도 사용 가능함
#   - 반복 횟수가 정해진 경우에도 사용 가능함
# ------------------------------------------------------------------


# [반복 횟수가 정해진 경우 while 반복문]
# Down-counting : 10, 9, 8, ...., 1
# 방법1 - for ~ in
for i in range(10,0,-1):
    print(i, end=" ")
print()


# 방법2 - while

count = 10

while count>0 :     # 
    
    print(count,end=" ")
    count -=1
print()



# GuGuDan 9 단 while 문으로 출력하기


num = 1 
dan = 9
print(f"----------[{dan}]------------")
while num < 10 :
    
    print(f"{dan}*{num} = {dan*num}")
    num +=1