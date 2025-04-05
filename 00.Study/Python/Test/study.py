# 1. 



def check_text_1():
	while True:
		print('종료는 q,Q')
		user = input('검색어 입력: ').strip()
	
		if user in ['q','Q']:
			break 

		text = '''Example Page
			Welcome to the Example Page
			This is a sample paragraph with text.
			Visit us at Example.com'''
		
		if user in text:
			print(f'{user} 단어는 원본 문자열에 존재합니다.')
			check_num = input('변경시 숫자 1을 입력해주세요').strip()
			if check_num.isnumeric:
				if int(check_num) ==1:		
					change = input('변경할 단어 입력').strip()
					if change:
						text = text.replace(user,change) 
						print(text)
			else:
				pass

		else:
			print(f'{user} 단어는 원본 문자열에 존재하지않습니다.')

check_text_1()

# 2. 

def text_up_low(text):
	text_list = text.split(' ')
	text_upper =''
	text_lower =''

	print(f'-'*100+'\n')
	print(f'단어의 개수 : {len(text_list)}')

	for i in text_list:
		#print(i)
		a = ''.join(i.upper())
		b = ''.join(i.lower())
		text_upper += " "+a
		text_lower += " "+b

	print(f'대문자 :{text_upper}')
	print(f'소문자 :{text_lower}')

text1 = 'I am studying Python Programming'

#text_up_low(text1)

# 3.

matrix =[[1,2,3],[4,5,6],[7,8,9]]

sum =0
for i in matrix:
	for j in i:
		print(str(j)+' ',end='')
		sum +=j
	print()

print(f'전체합 :{sum}')


#4.

import random as rd

def sort_list():
	list_value = []

	for i in range(1,11):
		value = rd.randint(1,50)
		list_value.append(value)
	print(list_value)

	list_value.sort()

	print(list_value)
	for i in list_value:
		print(f'{i}: {i*"*"}')

sort_list()

# 5.
