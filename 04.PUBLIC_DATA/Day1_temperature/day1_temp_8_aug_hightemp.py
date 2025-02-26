import	csv
import	matplotlib.pyplot as	plt
import koreanize_matplotlib
file = open('../Data/deagu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(file)
next(data)

aug = []

for row in data : 
    if row[0] !='' and row[4] != '':
        month = row[0].split('-')[1]
        if month == '08':
            aug.append(float(row[-1]))



file.close()


plt.hist(aug, bins=100, color='tomato')
plt.title('대구 8월의 최고 기온 히스토그램')
plt.xlabel('Temperature')
plt.ylabel("Counts")
plt.show()