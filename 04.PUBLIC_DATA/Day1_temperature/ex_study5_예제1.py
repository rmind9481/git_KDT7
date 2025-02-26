import csv


# 함수

def get_lowhigh_temp(data):
    '''최고 기온 및 최고 기온의 날짜 구하기
    '''

    header = next(data)

    lowest_temp = 100 # 최저 기온 값을 저장할 변수 초기화(가장 큰값)
    lowest_data =''   # 최저 기온의 날짜를 저장할 변수 초기화

    highest_temp = -999 # 최고 기온을 저장할 변수 초기화 (가장 작은 값)
    highest_data =''    # 최고 기온의 날짜를 저장할 변수 초기화

    for row in data:
        if row[3] =='':
            row[3] = 100
        row[3] = float(row[3]) 
        # csv 파일의 데이터는 문자열로 취급
        # float(문자열) : 문자열을 실수 형태로 변환
        # (산술 연산을 위한 변환)
        if row[4] == '':
            row[4] = -999
        row[4] = float(row[4])
    

        if row[3] < lowest_temp:
            lowest_temp = row[3]
            lowest_data = row[0] # 날짜: index[0]

        if	row[4]>	highest_temp:
            highest_temp =	row[4]
            highest_date =	row[0]


    print('-'*50)
    print(f'대구 최저 기온 날짜 : {lowest_data}, 온도: {lowest_temp}')
    print(f'대구 최고 기온 날짜 : {highest_data}, 온도: {highest_temp}')

def	main():

    file = open('../Data/deagu-utf8.csv', mode='r', encoding='utf-8-sig')
    data	=	csv.reader(file)

    get_lowhigh_temp(data)
    file.close()



main()








