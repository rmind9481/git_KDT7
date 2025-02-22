# 11. 삼성전자라는 변수로 50,000원을 바인딩해보세요.
# 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.

samsung = 50000

print(f"삼성전자 {samsung} : 10주 보유 : {samsung*10} 금액입니다.")




# 12. 다음표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가 PER 등을 바인딩해보세요.

market_capitalization = "298조"
price = 50000
per = 15.79

print(f"시가총액 : {market_capitalization}, 현재가 {price}, PER : {per}")

# 13. 문자열 출력
# 변수 s 와 t에는 각각 문자열이 바인딩 되어있습니다.

s = "hello"
t = "python"

print(s+"! "+t)

# 14. 파이썬을 이용한 값 계산

# 2 + 2 * 3

print(2 + 2 * 3)


# 15. type 함수


a = 128
print(type(a))

# 16. 문자열을 정수로 변환

num_str = "720"

num_str = int(num_str)

print(num_str)

# 17. 정수를 문자열 100으로 변환

num = 100
num = str(num)

print(num)


# 18. 문자열을 실수로 변환

# 문자열 "15.79" 를 실수(float) 타입으로 변환해보세요.

float_num = 15.79

# 19. 문자열을 정수로 변환

year = "2020"


# 20. 파이썬 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.
# 총 금액은 계산한 후 이를 화면에 출력해보세요.
price = 48584
moth = 36
total = moth *price

print(total,"원") 
