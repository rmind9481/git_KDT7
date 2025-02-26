# ------------------------------------------------------------------
#      str 타입 전용 함수 즉, 메서드(Method)
#   -  사용법 : 변수명.메서드명()
# ------------------------------------------------------------------
# [9] 문자열에서 앞부분, 끝부분 공백 제거 메서드
#   - 앞부분 공백 제거 : lstrip()
#   - 끝부분 공백 제거 : rstrip()
#   - 앞/끝부분 공백 제거 : strip()

data1 = '   Good Lcuk '


print(f"{data1} 원소 갯수 : {len(data1)} 개")


# 데이터 앞부분 공백 제거
data2= data1.lstrip()

print(f'{data2} 원소 갯수 : {len(data1)}개')



# 데이터 끝부분 공백 제거
data3= data1.lstrip()

print(f'{data3} 원소 갯수 : {len(data3)}개')

# 데이터 앞/끝부분 모두 공백 제거
data4= data1.strip()

print(f'{data4} 원소 갯수 : {len(data4)}개')


# [실습] 입력 데이터 여부 체크

data = input("댓글 입력 : ").strip()


print(f"입력 데이터 여부 : {len(data)}") 