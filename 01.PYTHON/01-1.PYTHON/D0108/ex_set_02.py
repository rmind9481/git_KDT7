# ---------------------------------------------------------------------
#   set 자료형 전용 함수 즉, 메서드
# ---------------------------------------------------------------------
#   set 데이터 생성
#   - 1 ~ 100 사이의 3의 배수로 구성된 data1 set
#   - 1 ~ 100 사이의 5의 배수로 구성된 data1 set


data1 = set(range(3,101,3))
data2 = set(range(5,101,5))

print(f"3의 배수 {data1}\n5의 배수 {data2}")



# [1] 2개의 집합에 모든 원소를 합치기 => 합집합 변수명.union(집합)
# -연산자 : | or
result1 = data1.union(data2)

print(f"result1 => {len(result1)}개, {result1}")
print(f"[합집합] data1 | data2  => {data1 | data2} \n")

# [2] 2개의 집합에 공통된 원소를 추출 => 교집합 변수명.intersection(집합)
# -연산자 : & 앰퍼센트 and
result1 = data1.intersection(data2)
print(f"result1 => {len(result1)}, {result1}")
print(f"[교집합] data1 & data2  => {data1 & data2} \n")



# [3] 1개의 집합에 공통된 원소를 추출 => 차집합 변수명.difference(집합)

result1 = data1.difference(data2)
print(f"result1 => {len(result1)}, {result1}")
print(f"[차집합] data1 - data2  => {data1 - data2} \n")

result1 = data2.difference(data1)
print(f"result1 => {len(result1)}, {result1}")
print(f"[차집합] data2 - data1  => {data2 - data1} \n")

