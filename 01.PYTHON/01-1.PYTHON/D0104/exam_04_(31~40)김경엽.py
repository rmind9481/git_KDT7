# 31 문자열 합치기

a = "3"
b = "4"

print(a+b)
# 문자열 str+str 이 합쳐져서 나올것이다.

# 32 문자열 곱하기

print("hi"*3)
# hihihi

# 33 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.

print("-"*80)


# 34 문자열 곱하기

t1 = "python"
t2 = "java"

# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.

# python java python java python java python java

t3 = t1+" "+ t2+" "

print(t3*4)

# 35 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때
#  % formatting을 사용해서 다음과 같이 출력해보세요.

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2= 13

print(" 이름 : %s 나이 : %d" %(name1,age1))
print(" 이름 : %s 나이 : %d" %(name2,age2))


# 36. 문자열 출력 
# 문자열 format()메서드를 사용해서 035번 문제를 다시 풀어보세요
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))


# 37. 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 38. 콤마 제거하기 
# 삼성전자의 상장주식수가 다음과 같습니다. 
# 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.

samsung_stock = "5,969,782,550"

n1 = int(samsung_stock.replace(",",""))

print(n1, type(n1))


# 39. 문자열 슬라이싱

msg = "2020/03(E) (IFRS연결)"

msg1 = msg[:7]
print(msg1)

# 40. strip 메서드
data = "   삼성전자    "
print(data.strip())