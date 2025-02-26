# --------------------------------------------------------------------------------
# 람다 표현식/ 익명함수/ 한줄 함수
# - 사용 목적 : 다른 함수의 인수로 전달되는 경우
# - 형식/문법: lamdba 매개변수들 : 실행 코드 및 반환값
# - 가장 많이 사용되는 함수 map(), filter(),...
# --------------------------------------------------------------------------------

# 일반 함수
def pluse_ten(x):
    return x+10

# 람다 표현식/ 람다 함수

lambda x :x+10

# 함수 호출/사용 ------------------------------------------------------------------
print(pluse_ten(1))

print((lambda x :x+10)(5))

print((lambda x,y :x+10)(5,10))


# 내장함수 map (함수명, 여러개의 대이터를 가지는 타입): 원소를 함수에 적용

datas = ['1','2','3']

datas2 = list(map(int, datas))

datas3 = []

for data in datas:
    datas3.append(int(data))

datas4 = [int(data) for data in datas]
print(datas,datas2)



# [1,2,3] ==> [2,5,10]
def calc(x):
    return x*x +1

result = list(map(calc, [1,2,3]))

print(result)

# 람다
result = list(map(lambda x:x*x+1, [1,2,3]))
print(result)