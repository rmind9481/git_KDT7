import pandas	as pd	
import csv
from tabulate	import tabulate


def print_head(title_list, max):
	count=1
	for title	in title_list:
		print(f'[{count:3d}]	{title}')
		if count	>=	max:
			break
		count +=1

def covert_datafrmae_totext(in_file, out_file):

	#csv에서 특정 컬럼만 읽기:	usecols=['column1',	'column2']	
	news_df =	pd.read_csv(in_file,usecols=['title','description'],encoding='utf-8-sig')
	#news_df는 ['title',	'description']	형태
	title_list = news_df.values.tolist()
	new_title_list =[]

	for title,	desc in title_list:
		total_desc = str(title) +'' +str(desc)
		new_title_list.append(total_desc)
		print_head(new_title_list,	5)
		#	text	file로 문자열을 저장
	with open(out_file,	'w') as file:
		for line	in new_title_list:
			file.write(line	+ "\n")


def main():
	in_file =	'인공지능_naver_news.csv'
	out_file1	=	'news_output1.txt'
	out_file2	=	'news_output2.txt'
	covert_datafrmae_totext(in_file,out_file1)
	#convert_csv_totext(in_file,	out_file2)
main()