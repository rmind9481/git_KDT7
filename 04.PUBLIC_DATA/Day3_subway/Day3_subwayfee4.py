import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

max = [0] *4
max_station = ['']*4
pic_count =	0
color_list =['#ff9999',	'#ffc000',	'#8fd9b6',	'#d395d0']	 #	파이 차트 컬러 값
label = ['유임승차','유임하차','무임승차','무임하차' ]


with open('../Data/3Day/subwayfee.csv',	encoding='utf-8-sig') as f:
	data = csv.reader(f)
	next(data)


	for row in data:
		for i in range(4,8):
			row[i] = int(row[i])

		plt.pie(row[4:8],labels=label,colors=color_list,autopct ='%.1f%%',shadow=True)
		plt.savefig('img/'+row[3]+'	'+row[1]+'.png')
		plt.close()	#	파일 닫기
		pic_count +=1
		if	pic_count >=10:
			break


