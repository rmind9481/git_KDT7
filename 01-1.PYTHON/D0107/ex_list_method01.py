# -------------------------------------------------------------------------
# List 자료형 전용 함수 즉, 메서드 살펴보기
# - 사용 : 변수명.메서드명()
# -------------------------------------------------------------------------

# 빈리스트 생성
datas = [] 


# 빈 리스트에 원소/요소 추가 => append(데이터)

datas.append(100)
print(datas)

datas.append("홍길동동")
print(datas)

datas.append(True)
print(datas)

datas.append([1,2,3,4,5])
print(datas)


# 원하는 위치에 원소/요소 추가 => insert(인덱스, 데이터)
datas.insert(1,"Good")
print(datas)


datas.insert(0,2025)
print(datas)

datas.insert(-1,2025) 
print(datas)


# 제일 마지막에 추가
datas.insert(len(datas),2025) 
print(datas)
