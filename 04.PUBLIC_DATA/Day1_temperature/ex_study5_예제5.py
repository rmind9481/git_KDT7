import	csv
import	matplotlib.pyplot as	plt
import koreanize_matplotlib

file = open('../Data/deagu-utf8.csv',	encoding='utf-8-sig')
data	=	csv.reader(file)
next(data)
result	=	[]
for	row	in	data	:
		if	row[-1]	!=	''	:	#	최고 기온을 리스트에 저장
			result.append(float(row[-1]))

file.close()
plt.figure(figsize=(10,	2))
plt.hist(result,	bins=500,	color='blue')	#	result에 저장된 값을 히스토그램으로 그림
plt.rcParams['axes.unicode_minus']	=	False	 #	레이블에 마이너스('-')기호 깨지는 현상 해결
plt.title("1907년 부터 2024년까지 대구 최고 기온 히스토그램")
plt.show()