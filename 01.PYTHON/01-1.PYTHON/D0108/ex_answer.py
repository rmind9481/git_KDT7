# --------------------------------------------
# Exam-05   : 1-3
# --------------------------------------------


# 중간고사 5과목 점수를 입력 받아 점수별로 구성된 리스트로 저장하세요.
# input() 함수는 1번만 사용하세요.

# jumsu = input("중간고사 5과목 점수 입력 \n(예: 99,80,70,70,60)")


# print(f"jumsu => {jumsu}")


# # 2. 5과목 1개의 str => 5개의 str로 분리 : split(',')
# jumsu_list = jumsu.split(',')
# print(f"jumsu_list => {jumsu_list}")


# # 3. 중간고사 평균을 출력 ==> 합계/과목수
# # str '90' => int 90
# jumsu_list[0] = int(jumsu_list[0])
# jumsu_list[1] = int(jumsu_list[1])
# jumsu_list[2] = int(jumsu_list[2])
# jumsu_list[3] = int(jumsu_list[3])
# jumsu_list[4] = int(jumsu_list[4])


# - 평균계산
# print(f"당신의 중간고사 평균 : {sum(jumsu_list)/len(jumsu_list):5.2f}")


# - 실수 와 자릿수
num = 123.1234567
print(num, round(num), round(num,0), round(num,1), round(num,5))


# - .숫자f => 소수점 숫자 자리만큼


# -----------------------------------------------------------------
#  Exam -5 : 1-3
# -----------------------------------------------------------------

msg = '2023년은 토끼해 입니다. 2024년은 무슨해 인가요? 나는 2024년이 기다려집니다.'

sIdx=msg.find('2')
eIdx=msg.find('년')
print(sIdx, eIdx)

year1 =msg[sIdx:eIdx]

print("year1",year1)

sIdx=msg.find('2',eIdx)
eIdx=msg.find('년',eIdx+1)
year2 =msg[sIdx:eIdx]
print(sIdx, eIdx)

print("year2",year2)

sIdx=msg.find('2',eIdx+1)
eIdx=msg.find('년',eIdx+1)
year3 =msg[sIdx:eIdx]
print(sIdx, eIdx)

print("year3",year3)