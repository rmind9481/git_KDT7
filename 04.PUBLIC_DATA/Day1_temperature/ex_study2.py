import csv


# encoding = 'utf-8-sig'로 \ufeff 제거 

#file = open(r'C:\Users\KDT17\Desktop\KDT_7\04.공공데이터\public_data\Data\daegudata.csv', mode='r', encoding='utf-8')
file = open('04.공공데이터/public_data/Data/daegudata.csv', mode='r', encoding='utf-8-sig')

#file = open('../Data/daegudata.csv', mode='r', encoding=None)
data = csv.reader(file, delimiter=',')
count=0

# newline ='' : 한 라인씩 건너 뛰며 저장되는 현상 없앰
fount = open('deagu-utf8.csv','w',newline='', encoding='utf-8-sig')
wr = csv.writer(fount)


for row in data: 
    for i in range(len(row)):
        row[i] = row[i].replace('\t','')
    print(row)
    wr.writerow(row) # writerow(row): 한 행씩 파일로 저장


file.close()
fount.close()
print('파일 저장 완료')