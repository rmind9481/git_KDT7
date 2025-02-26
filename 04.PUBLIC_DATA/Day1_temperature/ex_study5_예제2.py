import csv
import	numpy as np


# 함수  

def get_lowhigh_numpy(data):
    

    next(data)
    
    max_temp_list = list() # 최저 기온값 저장 리스트
    min_temp_list = list() # 최고 기온값 저장 리스트
    date_list = list() #날짜 정보 저장 리스트


    for row in data :
        if row[3] == '':
            row[3] = 100
        
        if row[4] == '':    # [-1]리스트에서 마지막 데이터가 없는경우
            row[4] = -999
    
        min_temp_list.append(row[3])
        max_temp_list.append(row[4])
        date_list.append(row[0])


    max_temp_array = np.array(max_temp_list)	 #	리스트를 ndarray로 변경
    max_temp_array = max_temp_array.astype(float) #	문자열 형태를 float으로 변경
    max_temp =	max_temp_array.max()	 #	최대값 리턴
    max_index =	max_temp_array.argmax()	

    min_temp_array = np.array(min_temp_list)	 #	리스트를 ndarray로 변경
    min_temp_array = min_temp_array.astype(float)
    min_temp =	min_temp_array.min()	 #	최소값 리턴
    min_index =	min_temp_array.argmin()	

    print(f'대구 최저 기온 날짜:	{date_list[min_index]},	온도:	{min_temp}')
    print(f'대구 최고 기온 날짜:	{date_list[max_index]},	온도:	{max_temp}')


def	main():
    
    file = open('../Data/deagu-utf8.csv', 'r', encoding='utf-8-sig')
    data = csv.reader(file)
    get_lowhigh_numpy(data)
    file.close()

main()