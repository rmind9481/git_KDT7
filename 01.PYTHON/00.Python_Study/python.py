# 기본 개념 문제 (1~10)
# 1. lambda 함수를 사용하여 두 숫자의 합을 구하는 함수를 작성하세요.



add = lambda x,y : x+y 

#print(add(3,8))


# 2. lambda 함수를 사용하여 주어진 숫자의 제곱을 반환하는 함수를 작성하세요.

a = lambda x : x**2

print(f"제곱: {a(3)}")


###
# 3. 세 개의 숫자를 입력받아 그중 가장 큰 값을 반환하는 lambda 함수를 작성하세요

three_nums = lambda x,y,z : max((x,y,z))

print(three_nums(3,5,15))

###

print((lambda x, y: x + y)(3, 5))

def get_max(x,y,z):
	return max(x,y,z)

print(get_max(5,10,35))


###

def get_max2(x,y,z):
	if x >= y and x >= z:
		return x
	elif y>= x and y >=z:
		return y
	else:
		return z

print(get_max2(50,3,7))


# 4. 문자열을 입력받아 해당 문자열의 길이를 반환하는 lambda 함수를 작성하세요.

str_input = lambda str_msg : len(str_msg)


print( str_input('파이썬 잘하고싶다.!!'))

# 5. 섭씨 온도를 입력하면 화씨 온도로 변환하는 lambda 함수를 작성하세요.

# [°F] = [°C] × 1.8 + 32

dgree = lambda x : (x*1.8)+32

print(f"섭씨 50  = 화씨 { dgree(50)}")


###
# 6. 리스트 [3, 1, 4, 1, 5, 9, 2]을 lambda와 sorted()를 이용하여 오름차순 정렬하세요.

list_b = [3,1,4,1,5,9,2] 


a_list = lambda x : sorted(x)
print(a_list(list_b))

# 7. 두 개의 리스트가 주어졌을 때, 같은 인덱스끼리 곱한 결과를 새로운 리스트로 반환하는 lambda 함수를 작성하세요.

a_list = [1,2,3,4,5]
b_list  =[11,22,33,44,55]

Double_list = lambda x,y : [x[i]*y[i] for i in range(len(x)) ]

print(Double_list(a_list,b_list))






# 8. 주어진 숫자가 짝수인지 홀수인지 판단하는 lambda 함수를 작성하세요.

# 9. 주어진 리스트에서 5보다 큰 숫자들만 필터링하는 lambda 함수를 작성하세요.

# 10. 문자열 리스트를 받아 문자열 길이 기준으로 정렬하는 lambda 함수를 작성하세요.


# 응용 문제 (11~20)
# 1. map()과 lambda를 사용하여 리스트 [1, 2, 3, 4, 5]의 모든 요소를 제곱한 새 리스트를 만드세요.
# 2. filter()와 lambda를 사용하여 리스트 [10, 15, 20, 25, 30]에서 20보다 큰 값만 필터링하세요.
# 3. reduce()와 lambda를 사용하여 리스트 [1, 2, 3, 4, 5]의 모든 요소를 곱하세요.
# 4. lambda를 이용해 주어진 문자열이 Palindrome(회문)인지 판별하는 함수를 작성하세요.
# 5. lambda와 sorted()를 이용하여 딕셔너리 { "apple": 3, "banana": 1, "cherry": 5 }를 값(value) 기준으로 정렬하세요.
# 6. lambda를 사용하여 주어진 리스트의 모든 요소에 2를 곱하는 함수를 작성하세요.
# 7. 두 개의 문자열을 입력받아, 두 문자열을 연결한 후 대문자로 변환하는 lambda 함수를 작성하세요.
# 8. lambda를 사용하여 주어진 리스트의 요소 중 첫 번째 문자가 'a'로 시작하는 단어만 필터링하세요.
# 9. 주어진 두 리스트의 동일한 인덱스끼리 더한 결과를 새로운 리스트로 반환하는 lambda 함수를 작성하세요.
# 10. lambda를 사용하여 주어진 숫자가 3과 5의 배수인지 확인하는 함수를 작성하세요.


# 심화 문제 (21~30)
# 1. lambda와 map()을 사용하여 리스트 [1, 2, 3, 4, 5]의 요소를 문자열로 변환하세요.
# 2. lambda와 filter()를 사용하여 주어진 리스트에서 소수를 찾아 반환하세요.
# 3. lambda와 map()을 사용하여 리스트에 있는 모든 문자열을 거꾸로 변환하세요.
# 4. 주어진 리스트에서 가장 긴 문자열을 찾는 lambda 함수를 작성하세요.
# 5. lambda를 사용하여 주어진 문자열의 모든 모음을 제거하는 함수를 작성하세요.
# 6. lambda를 사용하여 두 개의 리스트에서 같은 인덱스에 있는 요소의 차이를 구하는 함수를 작성하세요.
# 7. lambda를 사용하여 1부터 100까지의 숫자 중 7의 배수만 필터링하세요.
# 8. 주어진 문자열 리스트에서 대문자로 시작하는 단어만 필터링하는 lambda 함수를 작성하세요.
# 9. 리스트 [("John", 75), ("Jane", 82), ("Dave", 60)]에서 점수 기준으로 정렬하는 lambda 함수를 작성하세요.
# 10. lambda와 reduce()를 사용하여 1부터 10까지의 합을 구하세요.