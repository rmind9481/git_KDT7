# -------------------------------------------------------------------------
#   내장함수 len()
#   -데이터를 구성하는 원소 갯수를 알려주는 함수
#   - int, float, bool 사용못함
#   -여러개의 데이터로 구성된 데이터
#   ex) str타입
#   - 특징 : 여서 갯수를 알면 인덱스 범위를 알 수 있음
#   * 2개 => 인덱스 0 ~ 1
#   * 3개 => 인덱스 0 ~ 2
#   * n개 => 인덱스 0 ~ n-1
# -------------------------------------------------------------------------


data1 = 2025        #int
data2 = 3.5125234   #float
data3 = True        #bool
data4 = ''          #str


# 기본데이터 타입인 int, float, bool 은 1개의 데이터를 저장
# 원소/요소가 없음! ==> len()내장함수 사용 불가
# print(len(data1)) # ERROR

# 기본데이터 타입 중 str에서 사용
data4 = ''     
print(f"{data4} 원소 갯수 : {len(data4)}개")
print(data4)

data4 = 'a'     
print(f"{data4} 원소 갯수 : {len(data4)}개")
print(data4[0])

data4 = 'ab'     
print(f"{data4} 원소 갯수 : {len(data4)}개")
print(data4[0],data4[1])

data4 = 'abc'     
print(f"{data4} 원소 갯수 : {len(data4)}개")
print(data4[0],data4[1],data4[2])