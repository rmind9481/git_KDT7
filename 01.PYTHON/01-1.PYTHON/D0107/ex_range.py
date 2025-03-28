# ------------------------------------------------------------
# range 객체
# -기능 : 숫자의 범위 생성
# -형식 : range(숫자) =>  0 <= ~ < 숫자
#         range(시작숫자, 숫자) => 시작숫자 <= ~ < 숫자
# -원소/요소 : 인덱싱/슬라이싱
# -------------------------------------------------------------

# 1 ~ 100 로 구성된 리스트 생성
# nums = [1,2,3,4,5,6,......, 100]


nums = range(1,11)
print(type(nums), nums, nums[0], nums[-1], len(nums))

print(nums[1:6])

print("range => list 형변환", list(nums))

# 0 ~ 100 로 구성
nums = range(101)
print(type(nums), nums, nums[0], nums[-1],len(nums))
# 순서 있는 데이터 타입 즉, 시퀀스 데이터 타입의 특징
print(f"최대값 : {max(nums)} 최솟값 :{min(nums)}")
print(f"최대값 : {max(nums)} 최솟값 :{min(nums)}")


# 연사 => 덧셈, 곱셈, 맴버 연산자

r1 = range(1,6)            #1,2,3,4,5
r2 = range(10,16)          #10,11,12,13,14,15
print(f"덧셈 : {list(r1)+list(r2)}")
print(f"곱셈 : {list(r1)*2}")
print(f"맴버 연산자: { 3 in r1}")



# ---------------------------------------------------------------------
# 1 ~ 100 범위에서 3의 배수로만 구성된 데이터
# 3,6,9,12, 
# ----------------------------------------------------------------------

nums = range(3,101,3)

nums = list(nums)

print(f"nums 구성요소 : {nums}")


