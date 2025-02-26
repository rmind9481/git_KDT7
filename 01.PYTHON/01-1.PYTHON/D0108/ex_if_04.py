# [문] 시험 점수가 60점이면 합격, 아니면 불합격


jumsu = input("점수입력:").strip()

if len(jumsu)> 0 and jumsu.isdecimal():
    if int(jumsu) >= 60 :
        print('축하합니다. 합격입니다.')

    else:
        print("다시 한번 도전하세요.")
else:
    print("입력 데이터가 정확하지 않습니다.")