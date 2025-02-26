# -----------------------------------------------------------
# 영어 단어 맞추기 게임
# - 미리 영어 단어 선정
# - 사용자로부터 알파벳 a ~ z 까지 입력 대 소문자X
# - 입력된 알파벳에 해당하는 단어 부분은 알파벳 표시, 나머지 ■
# ----------------------------------------------------------


# FWORD = "apple"

# result = "■ "*len(FWORD)



# n =3 
# while n>0:

#     print(f'{result}')

#     in_al = input('a ~ z 1개 입력:').strip()

#     if in_al in FWORD:
#         result = ''

#         for al in FWORD:
            
#             if al == in_al:
#                 result = result + in_al
#             elif result not in ["■"+" "]:
#                 pass
#             else:
#                 result = result+"■ "

#         n-=1

      
FWORD = "apple"

result = list("■ "*len(FWORD))
print(result)


while True:
    in_w = input(f"a~z 까지 를 입력해주세요")

# 입력값의 단어가 있는지 체크
    for in_w in FWORD:

        # 단어가 있다면 => 그곳의 원소 자리에 접근
        if in_w in FWORD:
            # 인덱스 요소 찾기


            # a p p l e
            for w in FWORD:

                # 내가 입력한 값 == FWORD 안에 있는 문자랑 같다면 
                if in_w == w:
                    # ■ 거를 A 로 바꿘다. 
                    result=result+w
                    # 아니면 
                else:
                    result=result+'■'


        print(result)