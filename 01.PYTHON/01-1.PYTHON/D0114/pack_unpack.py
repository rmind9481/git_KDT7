# - 언팩킹 : 데이터들을 각가 하나의 변수에 따로 저장
# ------------------------------------------------------------------

# 팩킹 방식

nums = [1,3,5]
datas=5,6,7
keyValuse = {'name':'HONG','age':10}

print(nums,datas,keyValuse)
print('각 데이터의 0번 원소 =>', nums[0], datas[0],keyValuse['name'])

# 언팩킹으로 분리 ==> 변수 개수 == 데이터 개수

a,b,c = [1,3,5]
aa,bb,cc = 5,6,7

# 성과 이름을 분리해서 보기

phones = {'SKT': '011','kt':'016','lg':'019','신세기통신사':'107'}


items = phones.items()
# 팩킹
for item in items:
    print(f'{item[0]}통신사 => {item[1]}')

# 언팩킹
for k,v in items:
    print(f'{k}통신사 => {v}')

# 언팩킹 => 문법상 원소 개수만큼 변수 지정 => 
# 사용되지않는 데이터 저장 변수명 "_"
for k,_ in items:
    print(f'{k}통신사 => {_}')


