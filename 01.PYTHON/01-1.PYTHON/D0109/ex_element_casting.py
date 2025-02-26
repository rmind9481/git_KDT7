# -----------------------------------------------------
#   원소 단위 형변환
# -----------------------------------------------------

# 데이터 str 숫자

num_list = ['1','5','2','7','9']


# 원소의 합계 => sum() :숫자만 합계를 계산

num_list[0] = int( num_list[0] )
num_list[1] = int( num_list[1] )
num_list[2] = int( num_list[2] )
num_list[3] = int( num_list[3] )
num_list[4] = int( num_list[4] )


for idx in range(5) : # 0 <= ~ <5 : 0,1,3,4
    print(idx)


numRange = range(5)
print(numRange[0],numRange[1])

# ['good', 'luck',2025, False]

datalist = ['good', 'luck',2025, False]

# data = 0번 원소, 1번 원소,..., 3번 원소
for data in datalist:
    print(data)



