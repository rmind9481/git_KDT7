

# Split 함수
# - String Type 의 값을 나눠서 List 형태로 변환

items = 'zero on two three'.split()

print(items)

# ',' 을 기준으로 문자열 나누기

example = 'python,jquery,javascript'

print(example.split(','))

example = 'python,jquery,javascript'

a,b,c = example.split(',')

print(a,b,c)

# '.'
example= 'cs50.gachon.edu'

subdomain,domain,tld = example.split('.')

print(subdomain,domain,tld)

#==========================================

# join 함수
# - String List 를 합쳐 하나의 String 으로 변환

colors =['red','blue','green','yellow']

result = ''.join(colors)
print(result)

result = ' '.join(colors)

print(result)

result = '__'.join(colors)

print(result)

# List Comprehensions 

result = []

for i in range(10):
	result.append(i)

#####

result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i%2==0]
print(result)


#### List Comprehensions

word_1 = 'Python'
word_2 = 'good world'

result = [i+j for i in word_1 for j in word_2]

print(result)

###### 

case_1 = ['A','B','C']
case_2 = ['D','E','A']

result = [i+j for i in case_1 for j in case_2]
print(result)

result = [[i+j for i in case_1] for j in case_2]
print(result)


result = [i+j for i in case_1 for j in case_2 if not (i==j)]
print(result)

# 정렬
result.sort()
print(result)

# Enumerate 
# List 의 element 를 추출할때 번호를 붙여서 추출

for i, v in enumerate(['tic','tac','toe']):
	print(i,v)

mylsit = ["a","b","c","d"]
# list dml dlTsms index 와 값을 unpacking 하여  list 로 저장
print(list(enumerate(mylsit)))
#문장을 list 로 만들고 list 의 index 와 값을 unpacking 하여 dict 로 저장
dic = {i:j for i,j in enumerate('Gachon University is an academic institute\
						  located in South Korea.'.split())}
print(dic)


## Zip 
## 두개의 list 의 값을 병렬적으로 추출함

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for a,b in zip(alist,blist):
	print(a,b)

# 각 tuple 의 같은 index 끼리 묶음
a,b,c = zip((1,2,3),(10,20,30),(100,200,300))

print(a,b,c)

print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])

# Enumerate & Zip 

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']


for i , (a,b) in enumerate((zip(alist,blist))):
		print(i,a,b)         