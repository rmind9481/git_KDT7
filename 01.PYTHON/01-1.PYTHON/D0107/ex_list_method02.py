# -------------------------------------------------------------------------
# List 자료형 전용 함수 즉, 메서드 살펴보기
# - 사용 : 변수명.메서드명()
# -------------------------------------------------------------------------



datas = [9,5,-2,0,11]

# -원소/요소 를 순서를 뒤집기 => reverse()
# [9,5,-2,0,11]
# 
# [11,0,-2,5,9]

datas.reverse()
print(datas)


# -원소/요소를 정렬해 주는 메서드 => sort()
datas.sort()
print(datas)

# - 내림차순 정렬
datas.sort(reverse=True)
print(datas)

# - 원소/요소의 인덱스 찾아주는 메서드 => index()
# - 존재하지 않으면 ERROR 발생
# - 11의 인덱스

print('11의 인덱스 :', datas.index(11))
print('5의 인덱스 :', datas.index(5))
# print('7의 인덱스 :',datas.index(7))



# - 원소/요소 삭제 메서드 => remove(요소)

datas.remove(5)
print(datas)

