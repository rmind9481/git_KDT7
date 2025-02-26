import csv


# encoding = 'utf-8-sig'로 \ufeff 제거 

#file = open(r'C:\Users\KDT17\Desktop\KDT_7\04.공공데이터\public_data\Data\daegudata.csv', mode='r', encoding='utf-8')
file = open('../Data/daegudata.csv', mode='r', encoding='utf-8-sig')

#file = open('../Data/daegudata.csv', mode='r', encoding=None)
data = csv.reader(file, delimiter=',')
count=0

# next(): 한 행을 읽고 다음 행으로 이동
header = next(data)

print(header)

# 데이터 헤더 및 데이터 출력

i = 1
for row in data :
    print(row)
    if i >=5:
        break
    i +=1


file.close()


