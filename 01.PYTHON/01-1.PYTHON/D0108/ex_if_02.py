# -------------------------------------------------------------------
#   제어문 -조건문
#   - 특정  조건에 맞을 실행되는 코드 와 실행되지 않는 코드 분리 & 결정
#
# -------------------------------------------------------------------
# [문] 시험 점수가 60점이면 합격, 아니면 불합격


jumsu = 65

if jumsu >= 60 :
    print('축하합니다. 합격입니다.')

else:
    print("다시 한번 도전하세요.")


# [문] 숫자가 양수인지 음수인지 구분해서 출력해주세요.

num = 5


if num > 0 :
    print(f'{num}양수 입니다.')
    
else:
    print(f'{num}음수 입니다.')


# [문] 주민번호 '091203-1234567' 에서 나이를 계산해주세요.


jumsu = '091203-5234567'


# 7번 원소가 => 1,2,5,6 => 2000년도 이전
# 7번 원소가 => 3,4,7,8 => 2000년도 이후

# if jumsu[7] =='1' or jumsu[7] =='2' or jumsu[7] =='5' or jumsu[7] =='6' :

if jumsu[7] in '1256' :
    year = '19'+jumsu[:2]
    print(f"당신은 {year}년 생 입니다.")
elif jumsu[7] in '3478':
    year = '20'+jumsu[:2]
    print(f"당신은 {year}년 생 입니다.")
else:
    print("잘못된 주민등록 번호 입니다. 다시 하세요")






