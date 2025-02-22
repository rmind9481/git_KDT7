#  1. nums = [13, 21, 12, 14, 30, 18] 데이터에 대한 아래 코드 작성하세요.

nums = [13, 21, 12, 14, 30, 18]

#      (1)  nums의 모든 요소를 for반복문으로 출력

for i in nums :
     print({i})

#      (2)  nums에서 짝수값만 for반복문으로 출력

for i in nums :
    if i%2 ==0:
        print({i})

#      (3)  nums에서 모든 요소 값의 합계와 평균 출력

print(f'{sum(nums)/len(nums)}')
#      (4)  nums를 내림차순 정렬하여 모든 요소 출력
reversed(nums)
print(nums)

# 2. words = ["I", "study", "python", "language", "!"] 데이터에 대한 아래 코드
words = ["I", "study", "python", "language", "!"]
#      (1)  words의 모든 요소를 for반복문으로 출력

for i in words :
     print({i})

#      (2)  words에서 홀수번째 요소만 for반복문으로 출력

for i in words[1::2] :
        print(f'홀수번째 : {i}')

#      (3)  words에서 길이가 3이상인 요소만 for반복문으로 출력
              
for i in words:
    
    if len(i) >= 3:
        print(f'길이가 3이상 : {i}')

#      (4)  words를 오름차순 정렬하여 모든 요소 출력

words.sort()

print(words)

# 3.  아래 데이터에 대한 구현 코드 작성하세요.
#      files = ['intra.h', 'intra.c', 'define.h', 'run.py', 'ex01.py', 'intro.hwp']

files = ['intra.h', 'intra.c', 'define.h', 'run.py', 'ex01.py', 'intro.hwp']

#      (1) 확장자 없이 파일명만 출력
for i in files:
     print(i.split('.')[0])
#      (2) 확장자가 ‘h’이거나 ‘c’인것만 출력
for i in files:
    
     if i.endswith('.h') or i.endswith('c'):
          print(i)
#      (3) 파일명에 ‘e’가 2개이상 있고 ‘f’가 있는 파일명만 출력
for i in files:
    item = i.split('.')[0]
    if item.count('e') >=2 and item.count('f') >=1:
        print(item)

# 4. 1부터 N번 숫자까지 모두 곱하는 팩토리얼(Factorial)을 구현하세요.
#      [ 입력 ] 팩토리얼 숫자 :  5
#      [ 출력 ] 5! 결과 :  5 * 4 * 3 * 2 * 1  = 120

num = int(input("팩토리얼 할 숫자를 입력해주세요.").strip())

reslut = 1

for i in range(1,num+1):

    reslut *= i

print(f'{num}팩토리얼 {num} : {reslut}')      


#  5. for 반복문을 사용하여 2단부터 9단까지 모두 출력하세요.

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
    print()

#  6. 2개의 정수와 덧셈, 뺄셈, 곱셈, 나눗셈 연산자 1개를 입력 받으세요.

#   연산 결과를 출력합니다. 
#   단 종료하기 전까지 계속 메뉴를 요청하여 결과를 출력합니다.

num1=input("첫 번째 숫자 입력:").strip()
num2=input("두 번째 숫자 입력:").strip()
op=input("연산자 입력(+, -, *, /):").strip()


if len(num1)>0  and   len(num2)>0  and  len(op)>0:
    if (num1.isdecimal()) and (num2.isdecimal()) and (op in '+-*/'):
       
        num1=int(num1)
        num2=int(num2)

        ## (3) 입력한 연산자 종류에 따라서 연산 결과를 출력
        if op=='+':
            print(f'덧셈연산 : {num1} + {num2} = {num1+num2}')
        elif op=='-':
            print(f'뺄셈연산 : {num1} - {num2} = {num1-num2}')
        elif op=='*':
            print(f'곱셈연산 : {num1} * {num2} = {num1*num2}')
        else:
            if num2:
                print(f'나눗셈연산 : {num1} / {num2} = {num1/num2}')
            else:
                print(f'{num1}/{num2} => 0으로 나눌 수 없습니다.')
    else:
        print('숫자와 연산자(+,-,*,/)만 입력 가능합니다.')
else:
    print("입력된 데이터가 없습니다.")
    