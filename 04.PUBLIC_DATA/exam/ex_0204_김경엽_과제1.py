import csv

# CSV 파일 읽기


file = open('../Data/1Day/deagu-utf8.csv', mode='r', encoding='utf-8-sig')
data = csv.reader(file, delimiter=',')
next(data)

tropical_night = []

year = input("열대야를 계산할 연도를 입력하세요: ").strip()

#데이터 확인

for row in data:
    
    # 날짜가 0이 아니고 최저기온이 0이 아닌것들만
    if row[0] != '' and row[3] !='':
        # 사용자 년도가 맞으면 
        if row[0].split('-')[0] == year:
           # 6월에서 9월 체크
            if 6 <= int(row[0].split('-')[1]) <= 9 :
                # 최저 기온이 25도 이상인것들 
                if float(row[3]) >= 25:
                    #print(row)

                    #0000-00-00
                    # 월단위 슬라이싱
                    tropical_night.extend([row[0][5:],row[3]])
                    
              
print(f"{year}년 대구의 총 열대야 횟수: {len(tropical_night)}")

for i in tropical_night:
    print(i)


        


                





