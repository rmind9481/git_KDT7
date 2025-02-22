# ----------------------------------------------------------------
#   List 자료형 살펴보기
# ----------------------------------------------------------------
# [실습] 중간고가 점수를 입력 받아서 저장하기
# -5 과목 => jumsuList 저장

jumsuList = []


# - 점수 입력 받기

jumsu = input("중간고사 점수 입력: ").strip()

# str => int 형변환

jumsuList.append(int(jumsu))
jumsu = input("중간고사 점수 입력: ").strip()
jumsuList.append(int(jumsu))
jumsu = input("중간고사 점수 입력: ").strip()
jumsuList.append(int(jumsu))
jumsu = input("중간고사 점수 입력: ").strip()
jumsuList.append(int(jumsu))
jumsu = input("중간고사 점수 입력: ").strip()
jumsuList.append(int(jumsu))


# -합계와 평균 출력하기 ------------------------------

print(sum(jumsuList))
print(sum(jumsuList)/len(jumsuList))


# -새로운 점수 입력 받기 -----------------------------

jumsuList.clear()

