# -------------------------------------------------------------
#   [문제1] 주민번호를 입력 받아서 성별이 남자인지 여부를 출력하세요.
# 
#
#          -주민번호 : 000000-■000000
#           * 남자 : 1,3,5,7
#           * 여자 : 2,4,6,8
# -------------------------------------------------------------

# jumin = input("주민번호를 입력해주세요: ").split("-")


# print(f"주민번호 확인 {jumin}",type(jumin))
# print(jumin[1])

# gender_check = int(jumin[1][0])

# print(gender_check)

# print(f"성별이 남자 인가요? : {gender_check==1 or gender_check==3 or gender_check==5 or gender_check==7  }")


# jumin_2 = input('주민 번호 뒷자리 7자리를 입력해주세요 : ')

# gender_check = (jumin_2[0])
# print(f"주민번호 뒷자리 확인 {jumin_2}")
# print(f"성별이 남자 인가요? : {gender_check=='1' or gender_check=='3' or gender_check=='5' or gender_check=='7'  }")


# #  -주민번호 : 000000-■000000


# jumin = input("주민번호를 입력해주세요: ")


# print(f"주민번호 확인 {jumin}")
# print(jumin[7])

# gender_check = jumin[7]

# print(f"성별이 남자 인가요? : {gender_check=='1' or  gender_check=='3' or gender_check=='5' or gender_check=='7'  }")


# -------------------------------------------------------------
#   [문제2] 주민번호를 입력 받아서 나이를 계산해주세요.
# 
#           -단 2000년도 이후 출생자 입니다.
#          -주민번호 : 000000-0000000
#           * 남자 : 1,3,5,7
#           * 여자 : 2,4,6,8
# -------------------------------------------------------------


jumin = input("주민번호를 입력해주세요: ")

print(jumin)

age = int("20"+jumin[:2] )


print(f"{age} 년도에 태어났군요")

print(f"당신의 나이는 {2025-age}살 입니다")

