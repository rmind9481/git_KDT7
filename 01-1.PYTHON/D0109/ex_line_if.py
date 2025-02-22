# ---------------------------------------------------------------------------
# 조건
#   - if ~ else 문법을 4줄 -> 1줄 로 표현하는 문법
#   -문법 : 참 일때 실행 코드 if 조건문 else 거짓일때 실행코드
# ---------------------------------------------------------------------------


# [문] 양수, 음수 그뱔헤사 출력하기

num = 8

if num>0:
    print(f'{num} is 양수')

else:
    print(f'{num} is 음수')


print(f'{num} is 양수') if num>0 else print(f'{num} is 음수')


result = '양수' if num>0 else '음수'

print(f'{num} is {result}')

# [문] 양수,음수, 영 구별해서 출력하기

num=-4
if num>0:
    print('양수')
elif num<0:
    print('음수')
else:
    print('영')

# 다중조건문 => 조건부 표현식

print('양수') if num>0 else print('음수') if num<0 else print('영')


# [문] 월(month) 에 따른 계절을 알려주세요.

# 봄   : 3,4,5
# 여름 : 6,7,8
# 가을 : 9,10,11
# 겨울 : 12,1,2

# [1] 다중 조건문

num = 3

if num in range(3,6) :
    print('봄')
elif num in range(6,9):
    print('여름')
elif num in range(9,12):
    print('가을')
else:
    print('겨울')


# [2] 조건부 표현식

num = 8

season = '봄' if (num in range(3,6)) else '여름' if (num in range(6,9)) else(print('가을') if (num in [9,8,10]) else(print('겨울')))
print(f"season {season}")

month = 3

season = ''

if month in [3,4,5]:
    season='봄'
elif month in [6,7,8]:
    season='여름'
elif month in [9,10,11]:
    season='가을'
else:
    season='겨울' 

print(f'{month}은 {season}')