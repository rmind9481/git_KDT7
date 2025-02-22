# 1-1 비어있는 리스트에 10,40 "홍길동" , False,40, Fslse 를 저장하는 코드를 작성하세요.


msg_list = []

msg_list.append(10)
msg_list.append(40)
msg_list.append("홍길동")
msg_list.append(False)
msg_list.append(40)
msg_list.append(False)

print(msg_list)


# 1-2. 문제 1-1에서 생성된 데이터에서 모든 False 인덱스와 타입을 출력하세요.


print(msg_list[3], msg_list[-1] ,type(msg_list[3]),type(msg_list[-1]))


# 1-3 3. nums=[1,6,3,9,10]과 datas=[‘a’, ‘b’, ‘f’, ‘z’] 데이터의 덧셈 결과를 출력하세요.

nums=[1,6,3,9,10]
datas=['a','b','f','z']

n_list = nums+datas

print(n_list)

# 1-4. nums=[1,6,3,9,10] 데이터에 숫자 10을 곱셈한 결과를 출력하세요.


nums=[1,6,3,9,10]
print(nums*10)


# 1-5. 문제 1-3의 nums에 데이터를 사용하여 아래 요청사항을 코드로 작성해주세요.
#  - 모든 요소를 거꾸로 뽑아서 출력
nums.reverse()
print(nums)
#  - 3의 배수 번째 요소만 출력
print(nums[3::3])
#  - 짝수 번째 요소만 출력
print(nums[2::2])


# 2. 아래 데이터에서 밑줄___ 부분에 코드를 작성하세요.

nums=[]

nums.append(10)
nums.append(3)
nums.append(91)

print(f'nums 결과 :{nums} ')
nums.remove(3)
print(f'nums.remove(3) 결과 :{nums} ')
#nums.remove(100) => 에러
#print(f'nums.remove(100) 결과 : {nums.remove(100)}') 
nums.insert(1, 24)
print(f'nums.insert(1,24) 결과 : {nums}') 

# 3. 아래 데이터에서 요청을 처리하는 코드를 작성하세요.
nums=[1,2,3,1,2,3,5,6,7,3]

# * nums 변수의 데이터 개수 출력 코드 
print(len(nums))
# * 요소 값 3의 개수 출력 코드
print(nums.count(3))
# * 요소 값 6의 인덱스 출력 코드
print(nums.index(6))
# * 마지막 요소를 삭제하는 코드
del nums[-1]
print(nums)
# * 3번째 요소를 삭제하는 코드
del nums[3]
print(nums)

# 4. 아래 데이터 에서 요청에 대한 처리 코드를 작성하세요.

nums=[1,2,3,1,2,3]
data=['a','c']

#* 2개의 리스트를 합치는 2가지 방법의 코드를 작성하세요.

print(nums+data)

nums.append(data)

print(nums)

# 5. 아래 데이터에서 해당 결과가 나오도록 코드를 작성하세요.

data = [ 'a','c', True, 1, 9, 23, 'Happy', 21 ]

data.remove(21)
print(data)

data.remove("c")
data.insert(1,"b")
print(data)

data.insert(1,"2022")
print(data)

# 6. 데이터를 정렬하는 코드 작성하세요. 
# 오름차순 정렬과 내림차순 정렬 결과를 출력하세요.
datas=[9, 30, 1, 21, 5, 8, 0] 
datas.sort()
print(f"오름차순 {datas}")
datas.reverse()
print(f"내림차순 {datas}")



# 튜플 자료형(Tuple)을 다루는 문제

# 2-1. 튜플 자료형의 특징에 대해서 설명해 주세요. 
# 저장된 데이터 값을 오직 읽기만 가능하다
# 값을 변경하고 싶으면 형변환을 해서 값을 바꾸고 다시 튜플로 형변환해야된다.


# 2-2. 10, 30, 89, 10, 23, 1, 2, 7, 11 데이터를 변경이 불가능한 형태로 하나의 변수명에 저장해 
#  출력해 주세요

nums_tuple = 10, 30, 89, 10, 23, 1, 2, 7, 11


# 2-3. 문제 2-2에서 지정된 데이터의 값을 읽어와 출력해 주세요. 
# - 모든 요소를 하나씩 출력
print(nums_tuple)
# - 짝수 번째 요소만 출력
print(nums_tuple[2::2])
# - 3의 배수 번째 요소만 출력
print(nums_tuple[3::3])



# 2-4 아래 코드 실행 시 발생할 수 있는 상황 및 이유를 설명해 주세요.
# info= “211225-1234567”, “홍길동”, “남자” 
# info[1] =“Hong Gil Dong”

# 에러가 난다. 튜플은 안에 요소/원소를 변경 불가능하다.

# 2-5. 조건에 맞는 튜플(tuple) 객체 생성하세요. 
#  단, 2가지 방식으로 코드 작성하세요.

#  2022 1개 데이터를 year라는 튜플에 저장 하는 코드
year = 2022,
year =(2022,)

# * False 100 19.8 ‘Good’ 데이터를 datas라는 튜플에 저장하는 코드
data =  False,100,19.8, 'Good'
data =  (False,100,19.8, 'Good')

# 3. 종합 문제입니다.

# 3-1. 주민번호를 입력 받아서 아래 내용대로 출력해주세요.
# 0000년 0월 0일 생 00세
# (예시: 2000년 8월 2일 생 24세 )

jumin = input("2000년 생이상 주민번호를 입력해주세요 ex)000000-0000000 : ").strip()
jumin = jumin.split("-")

print(jumin[0])
jumin = jumin[0]
jumin_year = "20"+jumin[:2]
jumin_month = jumin[2:4]
jumin_day = jumin[4:]

print(jumin_year,jumin_month,jumin_day)

print(f"{jumin_year}년생 {jumin_month}월, {jumin_day} 일 생 {2025-int(jumin_year)}세 ")


# 3-2. 1~50사이 범위에서 3의 배수와 8의 배수로 구성된 데이터를 생성해 주세요. 
# 생성된 데이터에서 최대값, 최소값, 합계, 평균을 출력해 주세요.

data_3_8 = range(1,51,24)

print(data_3_8)
print(f" 최대값 {max(data_3_8)}, 최소값 {min(data_3_8)}, 합계{sum(data_3_8)}, 평균{sum(data_3_8)/len(data_3_8)}")