import csv
import	matplotlib.pyplot as plt



# 함수  

file = open('../Data/deagu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(file)


header = next(data)
result = []


for row in data:
    if row[4] != '':
        result.append(float(row[4]))


# 디버깅 용도

print(len(result))
plt.figure(figsize=(10,2))
plt.plot(result, 'r')
plt.show()


