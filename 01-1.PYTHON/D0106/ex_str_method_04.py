# -----------------------------------------------------
#      str 타입 전용 함수 즉, 메서드(Method)
#   -  사용법 : 변수명.메서드명()
# -----------------------------------------------------

# [3] 원소의 갯수 헤아리는 메서드 => count(데이터)

data = "HappyHappy"


# -'p' 가 data안에 몇 개 있는지 개수 헤아리는 메서드

print(f"p의 개숫 : {data.count('p')}개")


# -'pp' 가 data안에 몇 개 있는지 개수 헤아리는 메서드

print(f"pp의 개숫 : {data.count('pp')}개")



# -"P" 가 data안에 몇개 있는지 개수 헤아리는 메서드
print(f"P의 갯수 : {data.count('P')}개")


# [4] 특정 문자열을 다른 문자열로 변경하는 메서드
# => replace('예전', '새로운')
# - "H" => 'h'변경



data = "Happy Happy Happy Happy"
print(data.replace('H','h'))

print(data)

data = data.replace('H','h')
print(data)


# => 'h' => "H" 2개만 변경

print(data.replace('h','H',2))
print(data.replace('h','H',3))
print(data.replace('h','H',0))


#[실습] "에어컨 가격이 월 46,560,원 36개월"

data = "에어컨 가격이 월 46,560,원 36개월"
sindx = data.find('46')
eindx = data.find('원')

month = data[sindx:eindx]

print(f"month => {month} {month.replace(',','')}")


# -할부 개월 수 추출
count1 = data[data.find('36') : data.find('개월')]

sindx = data.find('36')
count2 = data[sindx:sindx+2]


print(count1,count2)