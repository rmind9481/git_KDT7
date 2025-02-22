# --------------------------------------------------------------
# [문] 숫자 2개와 4칙 연산자(+,-,*,/) 1개를 입력
#   받아서 연산 결과를 출력하세요.
#   [동작예시]
#   [입력] 숫자와 연산 방법 입력 : 9 8 +
#   [출력] 덧셈연산 : 9 + 8 = 17

#   [입력] 숫자와 연산 방법 입력 : 9 8 *
#   [출력] 덧셈연산 : 9 + 8 = 17

#   [입력] 숫자와 연산 방법 입력 : 9 0 /
#   [출력] 나눗셈 연산 : 0으로 나눌수 없습니다.
# ----------------------------------------------------------------



# num1,num2,msg = input('숫자 2개와 4칙 연산자("+,-,*,/") 1개를 입력 해주세요').split()

# print(num1,num2,msg)


# if len(num1) >0 and len(num2) and len(msg) :

#     if num1.isnumeric and num2.isnumeric    :
        
#         print('둘다 숫자 입니다.')
#         num1 = int(num1)
#         num2 = int(num2)

#         if msg in ('+,-,*,/'):
#             print('사칙연산 시작:')
            
#             if msg == '+':

#     else:
#         print('잘못 입력하셨습니다.')


#[방법1] 정상적인 입력을 한다는 전제

# (1) - 숫자 2개와 4칙 연산자(+,-,*,/) 1개를 입력 

num1 = input('1. 숫자 입력:').strip()
num2 = input('2. 숫자 입력:').strip()
op = input('연산자 입력(+,-,*,/):').strip()

#   num1 , num2, op 모두 입력 여부 ==> len() > 0 len()
#   num1 , num2 => 0 ~ 9 숫자 str ==> isdecimal()
#   op => +,-,*,/ 만 입력   ==> in

# (1-1) - 입력 데이터가 올바른 데이터인지 체크
if len(num1) > 0 and len(num2)>0 and len(op)>0:

    if num1.isdecimal() and num2.isdecimal() and op in '+-*/':
    # (2) str 타입의 숫자 데이터 => int 타입의 숫자 변환

        num1 = int(num1)
        num2 = int(num2)

        # (2) 입력한 연산자 종류에 따라서 연산 결과를 출력

        if  op == '+':
            print(f'덧셈연산 :{num1} + {num2} = ({num1+num2})')
        elif op == '-':
            print(f'뺄셈연산 :{num1} - {num2} = ({num1-num2})')
        elif op == '*':
            print(f'곱셈연산 :{num1} * {num2} = ({num1*num2})')
        else:
            if  num2: # 0 이면 애초에 False 라서 실행안됨
                print(f'나눗셈연산 :{num1} / {num2} = ({num1/num2})')
    else:
        print('정확한 데이터가 아닙니다.')

else:
    print('입력된 데이터가 없습니다.')


