# 1. 코드를 작성해 주세요.

# 1-1. 아래 데이터 jumsu 라는 변수명으로 저장해주세요.

# 점수 : 98 , 71,90,82,88

jumsu = [98,71,90,82,88]

# 1-2."Good Luck Happ New Year" 단어로 나누어 리스트로 저장하세요.
#    그리고 개수와 데이터를 출력하세요.


msg = "Good Luck Happ New Year"

msg_list = msg.split()

print(f"{msg_list} 원소 갯수 : {len(msg_list)}")

# 1-3. 중간고사 5 과목 점수를 입력 받아 점수별로 구성된 리스트로 저장하세요.
#       input() 함수는 1번만 사용하세요.

jumsu = []
jumsu = input("중간고사 점수 5과목을 입력해주세요 ex) 80,55,76,94,99 :").split(",")

print(jumsu)

# 1-4. [1,3,5,7,9,11] 를 [1,3,5,7,8,11,13,15] 가 되도록 리스트를 확장시켜주세요.

msg_list =  [1,3,5,7,9,11]

print(f"msg_list 원소 : {msg_list}")

msg_list.append(13)
msg_list.append(15)

print(f"msg_list 원소 : {msg_list}")
 

# 1-5. 리스트 [1,3,5,7,9,11] 에서 데이터 5를 꺼내는 코드를 작성해주세요.


msg_list = [1,3,5,7,9,11] 
print(msg_list.pop(2))


# 1-6. ['kiwi','banana','orange','apple'] 을 내림 차순으로 정렬해주세요.


fruits = ['kiwi','banana','orange','apple']
fruits.sort(reverse=True)
print(fruits)

# 1-7. [1,2,3,4,5,6] 리스트의 모든 요소를 삭제하는 코드를 작성해 주세요.

n1_list = [1,2,3,4,5,6]
print(n1_list)
n1_list.clear()
print(n1_list)

# 1-8.  ['가나다', '한글', '가방', '국가', '쏘핫']  에서 최댓값, 최솟값, 개수
#       를 출력하는 코드 작성하세요.


han_list = ['가나다', '한글', '가방', '국가', '쏘핫']

print(f"han_list 리스트: {han_list} \n최댓값 : {max(han_list)} 최솟값 : {min(han_list)} 개수 : {len(han_list)}")




# 2 아래 데이터를 검사하세요
data='hello@naver.com'
msg='123ABC'


# 2-1. data가 이메일 주소를 의미하는지 검사해 주세요
print(f"data가 이메일 주소를 의미하는지 : {'.com' in data}")
# 2-2. data가 알파벳으로 구성되었는지 검사해 주세요. 
print(f"data가 알파벳으로 구성되어있는지: {data.isalpha()}")

# 2-3. msg가 숫자로만 구성되었는지 검사해 주세요
print(f"msg가 숫자로만 구성되어있는지: {msg.isdigit()}")
print(f"msg가 숫자로만 구성되어있는지: {msg.isdecimal()}")

# 2-4. msg가 숫자와 영어로 구성되었는지 검사해 주세요
print(f"msg가 숫자와 영어로 구성되어있는지: {msg.isalnum()}")

# 2-5. msg가 공백으로 구성되었는지 검사해 주세요. 
print(f"msg가 공백 구성되어있는지: {len(msg) == 0}")


# 2-6  “!@Happy a Good Day~^^” 문자열을 시작과 끝을 검사해 주세요.
#       - 시작 :“!@” - 끝 : “^^”

msg = '!@Happy a Good DAy~^^'

print(f"{msg} \n'!@' 로 시작하는지 : {msg[:2] == '!@'} \n'^^' 로 끝나는지 :{msg[-1:] in '^^'} ")


# 2-7 아래 문자열에 나오는 숫자들을 모두 덧셈한 결과를 출력해 주세요. 
# 
# “2023년은 토끼해입니다. 2024년은 무슨 해 인가요? 나는 2024년이 기다려집니다.


msg = '2023년은 토끼해입니다. 2024년은 무슨 해 인가요? 나는 2024년이 기다려집니다.'


n1 = msg[msg.index("2023"):4]
n2 = msg[msg.index("2024"):msg.index("2024")+4]
n3 = msg[35:39]
print(f'{msg}안에 숫자들 : {n1,n2,n3}')

total = int(n1)+int(n2)+int(n3)

print(f"모든 수의 합:  {total}")

# n3 = msg[msg[msg.index("2024")+4].index("2024"):\
#          msg[msg.index("2024")+4].index("2024")+4]
