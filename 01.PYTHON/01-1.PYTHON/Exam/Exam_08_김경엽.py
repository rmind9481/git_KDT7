# ➀ 아래 데이터를 라는 변수명으로 저장해 주세요 그리고 총합 평균을 출력하세요

jumsu = {'국어': 98 ,"음악":71 , "미술":90, "체육":82, "과학":88}


data = jumsu.values()

print(f"총과목 점수: {jumsu }\n총합계 :{sum(data)} 평균 :{sum(data)/len(jumsu)}  ")


# 2. 

dic = {"김연아":"피겨스케이팅","류현진":"야구","박지성":"축구",'귀도':"파이썬"}


print(f"키만 {dic.keys()}")
print(f"값만 {dic.values()}")
print(f"둘다 {dic.items()}")


# 3. 3명의 사용자에 이름, 전화번호를 입력 받은 후 person 변수명에 저장하세요.

person = {}
for i in range(3):
    person = input("이름, 전화번호를 입력해주세요").strip().split(",")

print(person)

# 4. 한식 과 일식 값 출력

foods = {'한식':'불고기','중식':'짜장면','일식':'스시'}

print(f'한식 : {foods["한식"]}, 일식 : {foods["일식"]}')


# 5. 사용자로 부터 좋아하는 한식,중식,분식 입력받아서 데이터를 저장해주세요.

menu = input("좋아하는 한식, 중식, 분식 을 입력해주세요.")

foods = {'한식':'불고기','중식':'짜장면','일식':'스시'}

if menu in "한식" :
    print(foods[menu])
elif menu in "중식" :
    print(foods[menu])
elif menu in "일식" :
    print(foods[menu])
else :
    foods[menu] = 0
    print(foods)

# 6. {'류현진':'야구', '김연아':'피겨스케이팅','박지성':'축구', '귀도':'파이썬} 데이터에 
#   손흥민선수에 대한 데이터를 추가 후, 정렬해주세요.

person = {'류현진':'야구', '김연아':'피겨스케이팅','박지성':'축구', '귀도': '파이썬'}

person['손흥민'] = '축구'
       
print(person)

# 7. 빈데이터를 저장하는 코드를 리스트,튜플 딕셔너리, 집합, 문자열 등 각 데이터 타입에 따라 작성하세요.

data1 = set()
data2 = []
data3 = {}
data4 = tuple()

print(type(data1),type(data2),type(data3),type(data4))
# 8. 아래 데이터를 student 라는 변수명으로 저장하세요. 과목별 최고점수,최저점수

student = {'베트맨':{'국어':90,'수학':89,'윤리':98,'국사':99},
           '마징가':{'국어':82,'수학':71,'윤리':80,'국사':91},
           '슈퍼맨':{'국어':77,'수학':100,'윤리':92,'국사':90},
           '슈렉'  :{'국어':94,'수학':82,'윤리':93,'국사':71},
           '피오나':{'국어':78,'수학':99,'윤리':91,'국사':83},
           }

# 과목별 최고 최저 점수

print()

# 9. "Good Luck" 대한 알파벳 하나 하나에 대한 대문자를 요소로 하는 리스트 생성후 정렬해 주세요.

msg = "Good Luck"
msg_upper = []

for i in msg :
    if i.isupper():
        msg_upper.append(i)

print(msg_upper)

# 10. 1~50 범위에서 2의 배수 , 5의 배수 7의 배수로 구성된 데이터를 저장하세요.
#   그리고 데이터에서 값들을 하나의 리스트로 합쳐주세요.

num1 = range(1,50,2)
num2 = range(1,50,5)

data = list(num1)+list(num2)

print(data)