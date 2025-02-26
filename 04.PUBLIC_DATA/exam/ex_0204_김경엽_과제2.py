import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

# CSV 파일 읽기

file = open('../Data/1Day/deagu-utf8.csv', mode='r', encoding='utf-8-sig')
data = csv.reader(file, delimiter=',')
next(data)

tropical_night = []

#데이터 확인


for row in data:
    
    # 날짜가 0이 아니고 최저기온이 0이 아닌것들만
    if row[0] != '' and row[3] !='':

        # 1990 ~ 2024 선별  and 6~9월  
        if 1990 <= int(row[0].split('-')[0]) <= 2024 and 6 <= int(row[0].split('-')[1]) <= 9:
                #print(row)
                # 최저 기온이 25도 이상인것들 
                if float(row[3]) >=25:
                    
                    # 년도 카운팅 
                    tropical_night.extend([row[0][:4]])
                     
              


#print(tropical_night)


# 열대아 리스트에서 카운팅

count = {}
for value in tropical_night:
    try: count[value]  +=1
    except: count[value] =1
print(count)
# 1993 년 도  키 에 0을 줘야됨
count['1993']= 0


# 딕셔너리 키 정렬
count = sorted(count.items())
# 튜플 언팩킹 
i = 0
for item in count:
    if i < 10:
        print(f'{item[0]}년 :{item[1]}회 ',end='')
        i += 1
    else:
        print()
        i=0
    


# x축: 연도, y축: 열대야 횟수
years = [item[0] for item in count]
counts = [item[1] for item in count]

# 그래프 설정
plt.figure(figsize=(12, 6))  # 그래프 크기 설정
plt.bar(years, counts, color='blue')  # 막대 그래프 생성

# 그래프 레이블 및 제목 추가
plt.xlabel("연도")
plt.ylabel("열대야 횟수")
plt.title("1990년~2024년 대구 연도별 열대야 횟수")

# x축 눈금 회전 
plt.xticks(rotation=45)

# 그래프 표시

plt.show()
 



        

        


                





