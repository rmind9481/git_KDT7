# -----------------------------------------------------------------------
#   list 자료형
#   - 다양한 종류의 여러 개의 데이터를 저장하는 타입
#   - 형         식 : [ 데이터1, 데이터2, ....., 데이터n]
#   - 원소/요소 식별 : 인덱스 => 슬라이싱
# -----------------------------------------------------------------------


# List 데이터 생성
# - 빈 리스트 생성 : 원소/요소 0개

nums1 = []
nums2 = [1,2,3,4,5,6]

data1 ='2025'
data2 =100
data3 ='하늘'
datas = [data1,data2,data3]         # ['2025'주소, 100주소, '하늘' 주소]

print(datas)

# 타입 확인하기, 원소/요소 개수 확인
print(f"names1 => {type(nums1)},{len(nums1)}개")
print(f"names2 => {type(nums2)},{len(nums2)}개")
print(f"datas => {type(datas)},{len(datas)}개")


# - 리스트를 원소로 저장하는 리스트

names = ['홍길동','마징가','베트맨']
jobs = ['의적','로봇','박쥐']

datas2 =[names, jobs, 100, 200, False]


# 타입 확인하기, 원소/요소 개수 확인
print(f"names1 => {type(nums1)},{len(nums1)}개")
print(f"names2 => {type(nums2)},{len(nums2)}개")
print(f"datas => {type(datas)},{len(datas)}개")
print(f"datas2 => {type(datas2)},{len(datas2)}개")
