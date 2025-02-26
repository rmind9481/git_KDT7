# ---------------------------------------------------------------------
#   set 자료형 살펴보기
#   - 특징 : 중복 데이터 저장 불가!     순서 없음!
#   - 형식 : {데1,데2,...., 데n}
#       {} <= 빈 dict , set() <= 빈 set
# ---------------------------------------------------------------------


# [1] set 데이터 생성


data1 = {1,1,2,23,4,5,5,5,6,8}
data2 = {'A', 100, False,100, 100, False, 'A', 'A'}
data3 = {'홍길동', (10,20,30), False}
data4 = {}
data5 = set()
# 데이터 확인

print(type(data1), len(data1), data1)
print(type(data2), len(data2), data2)
print(type(data3), len(data3), data3)
print(type(data4), len(data4), data4)
print(type(data5), len(data5), data5)


