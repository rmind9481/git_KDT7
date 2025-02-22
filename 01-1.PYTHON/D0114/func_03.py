# --------------------------------------------------------
# 키워드 파라미터 함수
# - 매개변수 개수 : 0개 ~ n 개 인자
# - 매개변수 형태 : def 함수명(** 매개변수명)
# - 매개변수 타입 : dict 타입
# --------------------------------------------------------

# [실습] 중간고사 3과목 점수에 대한 합계와 평균을 출력하는 함수

# ------------------------------------------------------------
# 함수기능 : 3과목 대한 합계와 평균 출력
# 함수이름 : jumsu_sum_avg
# 매개변수 : jumsu1, jumsu2, jumsu3
# 함수결과 : 합계 와 평균
#-------------------------------------------------------------

def jumsu_sum_avg (jumsu1,jumsu2,jumsu3):
    total = jumsu1+jumsu2+jumsu3
    avg = total/3
    return total, avg


# ----------------------------------------------------------
# 함수기능 : 0개 ~ n개 과목에 대한 합계와 평균 출력
# 함수이름 : jumsu_sum_avg2
# 매개변수 : *jumsu
# 함수결과 : 합계 와 평균
# ------------------------------------------------------------

def jumsu_sum_avg2 (*jumsu):
    total = sum(jumsu)
    avg = total/len(jumsu) if len(jumsu) else 0
    return total,avg


jumsu_sum_avg2()
jumsu_sum_avg2(100,90,70,99)
jumsu_sum_avg2()


# ----------------------------------------------------------
# 함수기능 : 과목별 0개 ~ n개 과목에 대한 합계와 평균 출력
# 함수이름 : jumsu_sum_avg3
# 매개변수 : **jumsu
# 함수결과 : 합계 와 평균
# -----------------------------------------------------------

# def jumsu_sum_avg3(**jumsu):
#     print(type(jumsu))
#     total = 0
#     for v in jumsu.values():
#         total +=v

def jumsu_sum_avg3(**jumsu):
    print(type(jumsu))
    total = sum(jumsu.values())
    avg = total/len(jumsu) if len(jumsu) else 0
    print(total,avg)


# 가변이면서 키워드/키를 가진 매개변수

jumsu_sum_avg3(music=90, art=100, kor=98, eng=99,math = 100)

{}.update(name='hong')


