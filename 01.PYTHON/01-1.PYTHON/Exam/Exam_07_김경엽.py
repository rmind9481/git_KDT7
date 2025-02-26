#  1. 코드를 작성해 주세요. 
# ➀ 1,5,3,9,1,1,2,8,7,4,2 데이터 중복 제거 후 저장하고 타입, 개수, 데이터 출력하세요.

data = [1, 5, 3, 9, 1, 1, 2, 8, 7, 4, 2]
unique_data = set(data)
print(f"타입: {type(unique_data)}, 개수: {len(unique_data)}, 데이터: {unique_data}")

# ➁ [1,1,5,2,6,9,2]와 [5,9,1,3,4,2,8,7,1,2,5] 데이터를 중복된 값을 제거한 하나의 리스트를
# 생성해 주세요.
list1 = [1, 1, 5, 2, 6, 9, 2]
list2 = [5, 9, 1, 3, 4, 2, 8, 7, 1, 2, 5]

list_total = list(set(list1).union(set(list2)))

print(list_total)


# ➂ ‘Happy Christmas’ 문자열에서 알파벳만 중복을 제거한 데이터로 저장해 주세요.
string = "Happy Christmas"
set_string = set(string)

print(set_string)

# ④ 1부터 6까지의 값을 가진 데이터 num6, 4부터 9까지의 값을 가진 데이터 num9에서 
# num6에만 존재하는 데이터를 출력하세요. 그리고 num6와 num9에 모두 존재하는 
# 데이터를 출력하세요. 그리고 num6와 num9의 모든 데이터를 중복 없이 출력하세요.

num6 = set(range(1,7))
num9 = set(range(4,10))

print(f'차집합 : {num6.difference(num9)}')
print(f'교집합 :{num6.intersection(num9)}')
print(f'합집합 :{num6.union(num9)}')

# ⑤ [9, 3, 1, 8, 7, 2, 1, 4, 2, 3, 5, 7] 에서 중복된 데이터 제외한 데이터들 평균 출력

num = [9, 3, 1, 8, 7, 2, 1, 4, 2, 3, 5, 7]

num = set(num)

print(sum(num)/len(num))

# ⑥ 집합 1,2,3 데이터에 [4,5,6,7,8] 데이터를 한꺼번에 추가 해 주세요.
num1 = [1,2,3]
num2 = [4,5,6,7,8]

print(num1.append(num2))


# ⑦ 데이터 {'name':'pey', 'phone':'0119993323', 'birth': '1118'}에서 메서드를 사용해서
# 1118과 pey를 출력하세요. 그리고 gender에 대한 값을 출력하세요. 

# 조건) 값이 없을 경우 no-data라고 출력하세요

data = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

print(data['name'] ,data['birth'])


if data.get('gender') == None :
    print('no-data')


#  ⑧ True, False 2가지 데이터만 저장하는 타입은 ( )입니다.

#  정답은 : Bool 타입


#  ⑨ 아래 데이터를 논리 데이터 타입으로 저장 후 출력하세요.
    
# 데이터
# ‘Happy’
#  ‘’
#  [12]
#  []
#  ( ‘A’ )
#  ( )
#  { 1:89, 2:12 }
#  { }
#  1
#  0
#  None
#  set()

data = [
    bool("Happy"),
    bool(""),
    bool([12]),
    bool([]),
    bool(('A',)),
    bool(()),
    bool({1: 89, 2: 12}),
    bool({}),
    bool(1),
    bool(0),
    bool(None),
    bool(set())
]
print(data)


#  ⑩ 3명의 학생 정보를 입력 받아서 저장해 주세요.
#      - 학생 정보 :  학번, 이름, 전공, 학년


students=()
s1=input('학번, 이름, 전공, 학년:').split()
s2=input('학번, 이름, 전공, 학년:').split()
s3=input('학번, 이름, 전공, 학년:').split()

s1_dict = {'학번':s1[0], '이름':s1[1], '전공':s1[2], '학년':s1[3]}
s2_dict = {'학번':s2[0], '이름':s2[1], '전공':s2[2], '학년':s2[3]}
s3_dict = {'학번':s3[0], '이름':s3[1], '전공':s3[2], '학년':s3[3]}