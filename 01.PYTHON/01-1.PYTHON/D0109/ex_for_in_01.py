# -----------------------------------------------------------------------
#
#   제어문 - for ~ in 반복문
#
#   -특징
#   * 반복 횟수가 정해진 경우 거의 사용됨
#   * 여러개의 원소/요소 를 가지는 데이터 타입의 경우
#     원소/요소 추출에 사용됨
# -----------------------------------------------------------------------
#    -형태 
#   for 변수명 in 데이터 :    <= 여러개의 데이터를 저장 타입
#   반복적으로 실행할 코드  
#
# -----------------------------------------------------------------------

# [1] str 타입과 반복문

msg = 'Merry Christams~'

#   - 원소 한개씩 출력

# print(f'[0번 요소] {msg[0]}')
# print(f'[1번 요소] {msg[1]}')
# print(f'[2번 요소] {msg[2]}')
# print(f'[3번 요소] {msg[3]}')
# print(f'[4번 요소] {msg[4]}')
# print(f'[5번 요소] {msg[5]}')
# print(f'[6번 요소] {msg[6]}')
# print(f'[7번 요소] {msg[7]}')
# print(f'[8번 요소] {msg[8]}')
# print(f'[9번 요소] {msg[9]}')
# print(f'[10번 요소] {msg[10]}')
# print(f'[11번 요소] {msg[11]}')
# print(f'[12번 요소] {msg[12]}')
# print(f'[13번 요소] {msg[13]}')
# print(f'[14번 요소] {msg[14]}')
# print(f'[15번 요소] {msg[15]}')



# -msg를 코드값으로 출력하세요 => ord()

# 개선 => 반복문 17번 횟수, 요소/원소 추출
#   char = msg[0],  =   msg[0],......., = msg[16]
for char in msg:
    print(char)

# -msg를 코드값으로 출력하세요 => ord()
for char in msg:
    print(ord(char), end=".")
   
# -msg를 코드값으로 출력하세요 => ord()
print()
for char in msg:
    print(bin(ord(char))[2:],end=".")


# 숫자 str 데이터로 구성된 msg
print()
msg = '1 3 5 7 9 11 22'

msg_list = msg.split()
print(msg_list)

# - 리스트의 모든 원소를 int로 형변환 => int(원소값)
# - 원소 값 변경이 되어야 하는 경우는 인덱스를 반복문으로 추출
#   num = '1','2','3','4','5'
#   num ='1' , '3', '5',.....
for idx in range(len(msg_list)):
    msg_list[idx] = int(msg_list[idx])

print(msg_list)
# nums = ['1','3','5','6','7']

# # casting str num => int num -------------------
# for num in nums :
#     nums = int(num)


# # update list : str  num ==> int num ---

# for idx in range(len(msg_list)):
#     num[idx] = int(num[id])