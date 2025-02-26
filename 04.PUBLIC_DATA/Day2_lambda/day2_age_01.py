import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib 
import re

file = open('../Data/2Day/age.csv', encoding='euc_kr')

data = csv.reader(file)
header = next(data)

result = []
city = ''
for row in data:

    if "산격3동" in row[0]:
        str_list = re.split('[()]',row[0])

        print(str_list)
        for data in row[3:]:
            data = data.replace(',','')
            result.append(int(data)) 

file.close()
print(result)

plt.title(f'{city} 인구현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()