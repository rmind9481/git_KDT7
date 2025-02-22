# -----------------------------------------------------------------
# List 자료형 과 내장함수
# - 원소/요소를 인덱스로 식별 => 순서있는 자료형/Sequence Type
# -----------------------------------------------------------------

nums = [11,22,33,44,55,0,321,4,2,35,2,5223,5555]
names = ["홍","박","이"]

# [1] 원소/ 요소 갯수 헤아리는 len()

print(f"nums 원소 갯수 : {len(nums)} 개")
print(f"names 원소 갯수 : {len(names)} 개")


# [2] 원소/요소 중 최댓값/ 최솟값 구하는 함수 max(), min()
print(f'nums 최소/최대 원소 : {min(nums)}, {max(nums)}')
print(f'names 최소/최대 원소 : {min(names)}, {max(names)}')

# [3] 원소/요소의 합계 구하는 함수 sum() : 수치타입의 요소일 경우만 가능
print(f"nums 원소 합계 : {sum(nums)}")
# print(f"names 원소 합계 : {sum(names)}") <= 불가

print(f"nums 원소 합계 평균: {sum(nums)/len(nums)}")

#[4] 원소/요소 정렬하는 내장 함수 sorted()
# - 오름차순 정렬 : 0,1,2,,...... / ㄱ,ㄴ,...... ㅎ / a,b, ...,z
# - 내림차순 정렬 : 10,9, ......,0 / ㅎ, ㅍ, ....ㄱ /z,y,.....,a


# 숫자 정렬
result = sorted(nums)
print(nums, result, sep="\n")

result = sorted(nums, reverse=True)
print(nums, result, sep="\n")

# 문자 정렬
result = sorted(names)
print(names, result, sep="\n")

result = sorted(names, reverse=True)
print(names, result, sep="\n")

# ==> str 타입 데이터의 정렬

msg = "Happy" 
result = sorted(msg)
print( msg, result, sep="\n")


msg = "Happy" 
result = sorted(msg, reverse=True)
print( msg, result, sep="\n")

msg = ["Happy"] # => 원소 1개로 인식
print(msg[0][0])