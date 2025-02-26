# -----------------------------------------------------------------------
#   Tuple 자료형
#   - 특징 : 여러종류의 여러개의 데이터 저장 가능
#               단, 저장 후 수정, 변경, 삭제, 추가 불가!!
#   - 활용 : 변경이 되면 안되는 데이터 저장 시 사용함!
#   - 원소/요소 : 인덱싱과 슬라이싱 
# -----------------------------------------------------------------------

# - 튜플 데이터 생성

datal = ()          # 원소 0개 빈튜플
data2 = ('F')
data3 = "f",
data4 =(10,False,"Good")
data5 =10,False,"Good"  # 여러개가 있을때는 , 를 안찍어도 된다.
data6 = [10, "Good"]

# - 튜플 데이터 생성
print(type(datal), type(data2))
print(len(datal), len(data2))

data2 = ('F',)  # 단일 원소에 , 를 찍어줘야 된다.

# -타입, 원소 갯수 출력

print(type(datal), type(data2),type(data3),type(data4),type(data5))
print(len(datal), len(data2), len(data3), len(data4))


# -원소/요소 읽기 => 변수명[인덱스]
print(data2[0],data3[-1], data4[0], data5[-1])



# -원소/요소 값 변경 => 변수명[인덱스] => 새로운 값
# => List 경우
print("LIST", data6[0])
data6[0] = "백"
print("LIST", data6[0])
 
# => Tuple 경우 ==> 미지원 기능 불가!
# print("TUPLE", data5[0])
# data6[0] = "백"
# print("TUPLE", data5[0])


# - 원소/요소 값 삭제 => del 변수명[인덱스]
# del data6[0]
# print("List", data6[0], data6)

# del data5[0]
# print("TUPLE", data5[0], data5)


# --------------------------------------------------------------------
# 반드시 변경이 필요한 경우 는 list 형 변환 후 변경
#   Tupple 형 변환 
# --------------------------------------------------------------------

data =("F", 'Park')


# 성별 'F' ==> 'M' 변경 : list() 형변환
data = list(data)

print((f'data => {type(data)}'))

# 원소 값 변경
data[0] = 'M'

# list => tuple() 형 변환
data = tuple(data)
print(f'data => {type(data), {data}}')