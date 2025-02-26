import csv 
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib


def draw_lowhigh_graph(start_year, month, day):
    file = open('../Data/deagu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(file)

    next(data)
    
    high_temp = []
    low_temp = []
    x_year = []
    
    for row in data :
        if row[-1] != '' :
            date_string = row[0].split('-')
            if int(date_string[0]) >= start_year:
                if int(date_string[1]) == month and int(date_string[2]) == day :
                    high_temp.append(float(row[-1]))
                    low_temp.append(float(row[-2]))
                    x_year.append(date_string[0])

    file.close()



    plt.figure(figsize=(20,4))
    plt.plot(x_year, high_temp, "hotpink", marker='o', label= '최고기온')
    plt.plot(x_year, high_temp, "royalblue", marker='S', label= '최저기온')


    plt.rcParams['axes.unicode_minus'] = False
    plt.title(f"{2000}년 이후 {7}월 {20} 일의 온도 변화 그래프", size =16 )


plt.legend(loc=2)
plt.xlabel('year')
plt.ylabel('temperature')
plt.show()

draw_lowhigh_graph(2000,7,26)
