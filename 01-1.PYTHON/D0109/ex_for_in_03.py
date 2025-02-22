# ------------------------------------------------------------------
# [실습] 좋아하는 숫자를 10명의 사람에게 입력 받은 후
#   숫자들을 저장해 주세요.
#   그리고 가장 많은 사람들이 좋아하는 숫자가 무엇인지
#   출력해주세요.
#
# ------------------------------------------------------------------


# numbers = []



# for count in range(10):
#     num = input("좋아하는 숫자는?").strip()
#     numbers.append(int(num))

# print(numbers)

# 숫자별로 카운팅
fnums = [3,6,1,1,1,3,6,8,9,9,9,9,9,9,9,9,9,9]

countDict={}

for num in fnums:
    # Key  = num
    # value = fnums.count(num)
    # fnums.count(num)
    # print(f'[{num}] - {fnums.count(num)}개')
    if num not in countDict.keys():
        countDict[num] = fnums.count(num)

print(countDict)

# 가장 많은 숫자를 찾기

max_key = []
max_value = 0

for item in countDict.items():
    if max_value ==item[1]:
        max_key.append(item[0])
    if max_value<item[1] :     
        max_key.clear()           # 0<1          1<4
        max_key.append(item[0])   # 숫자_2        숫자_3
        max_value=item[1]         # 1             4

print(f" 가장 좋아하는 숫자는 {max_key}({max_value})번")
