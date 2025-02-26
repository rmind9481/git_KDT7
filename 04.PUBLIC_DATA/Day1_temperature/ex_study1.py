import csv



#file = open(r'C:\Users\KDT17\Desktop\KDT_7\04.공공데이터\public_data\Data\daegudata.csv', mode='r', encoding='utf-8')
file = open('../Data/daegudata.csv', mode='r', encoding='utf-8')
#file = open('../Data/daegudata.csv', mode='r', encoding=None)
data = csv.reader(file, delimiter=',')
count=0


# # CSV 파일에서 한 라인씩 읽어옴
for row in data:
    if count > 5:
        break
    else:
        print(row)
    count+=1

#print(data) # csv_reader 객체 출력

file.close()
