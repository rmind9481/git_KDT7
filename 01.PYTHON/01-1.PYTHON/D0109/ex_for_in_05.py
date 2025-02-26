# ---------------------------------------------------------------------
# Comprehesion
# - for ~ in + if + List/Set/Dict 결합한 문법
# - 시간과 메모리 상의 이득으로 아주 많이 사용됨
#
# ---------------------------------------------------------------------

# str 타입 숫자 를 여러개 저장한 List 
# int 타입 숫자로 변환한 새로운 List 만들기

data1 = ['11','22','33']
data2 = []


for num in data1 :
    data2.append(int(num))

    
print(data1,data2, sep='\n')


# [] 와 for 결합

data3 = [ int(num) for num in data1 ]
print(data1,data2,data3, sep='\n')



# ---------------------------------------------------------
# 숫자 데이터를 저장하고 있는 List 에서 2의 배수인 숫자만
# 새로운 List에 원소로 넣기

data1 = [3,8,2,9,5,11]
data2 = []

for num in data1:
    if not num%2 == 0 :
        data2.append(num) 

# [] 와 for 와 if 결합
data3=[ num for num in data1 if num%2==0]
#           -----(1)--------
#                num   ===> -----(2)-----
#       -(3)- num <===  True일때




# ---------------------------------------------------------
# 숫자 데이터를 저장하고 있는 List 에서 2의 배수인 숫자는 제곱해서 
# 전달하고, 2의 배수가 아닌 숫자는 그대로 전달해서 
# 새로운 List에 원소로 넣기

data1 = [3,8,2,9,5,11]
data2 = []

for num in data1:
    if not num%2 == 0 :
        data2.append(num) 

# [] 와 for 와 if 결합
data3=[ num**num if num%2==0 else num for num in data1 ]
#                                -----(1)--------
#      -----(2)-----        <====  num   
