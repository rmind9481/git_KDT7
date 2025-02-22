# ------------------------------------------------------------------
#   제어문 - while 반복문
#   - 반복 횟수가 미정인 경우에도 사용 가능함
#   - 반복 횟수가 정해진 경우에도 사용 가능함
# ------------------------------------------------------------------

# 리스트 데이터에 원소를 출력하기


data_list = ['하늘','가을','고양이', '책']


# 방법1) for ~ in

for data in data_list:
    print(data)



# 방법2) while => 원소 인덱스 지정

nums = len(data_list) # 리스트의 요소 갯수
idx = 0


while idx <nums: # 0<4
    print(data_list[idx], end=" ")
    idx +=1



# 2단 ~ 9단 while 문 사용 -----------------------

dan = 2

while dan<10 :
    print(f" ---- [{dan} 단] ----")
    num = 1
    while num < 10:
        print(f"{dan}*{num}= {dan*num}")

        
        num +=1
    dan +=1