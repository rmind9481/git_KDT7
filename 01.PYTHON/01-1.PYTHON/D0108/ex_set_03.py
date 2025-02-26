# ---------------------------------------------------------------------
#   set 자료형 전용 함수 즉, 메서드
# ---------------------------------------------------------------------



data1 = set(range(5,101,5))

print(f"data1 => {len(data1)} 개, {data1}")



# [4] 원소 1개 추가하는 메서드 => add()

data1.add(1000)
print(f"data1 => {len(data1)} 개, {data1}")

# [5] 원소 여러개 추가하는 메서드 => update()

data1.update(["A","B","A","A","C"])
print(f"data1 => {len(data1)} 개, {data1}")


# 에러  
# - 원소 단위의 데이터 타입이 List 불가

# data1.update(["A","B","A","A","C",[111,222]])
# print(f"data1 => {len(data1)} 개, {data1}")

# - 원소 단위의 데이터 타입이 Dict 불가

# data1.update(["A","B","A","A","C",{'name':'홍길동' }])
# print(f"data1 => {len(data1)} 개, {data1}")

data1.update(["A","B","A","A","C",(111,222)])
print(f"data1 => {len(data1)} 개, {data1}")



# [6] set 데이터에서 원소/요소 꺼내기 즉, 삭제됨 ==> pop()

print(data1.pop())
print(f"data1 => {len(data1)} 개,  data1.pop() {data1}")

# [7] set 데이터에서 원소/요소 삭제 ==> remove()

data1.remove("A")

# [8] set 데이터에서 모든 원소/요소 삭제 ==> clear()
data1.clear()
print(data1)