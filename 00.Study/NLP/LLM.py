# 훈련데이터 준비
# 준비한 텍스트 파일을 읽어 들여서 정리한 후에 앞에 Cleaned_ 가 붙은 파일 이름으로 정리합니다.


# ex) alice.txt => cleaned_alice.txt

# 캐글 해리포터 책 
# 캐글 엘리스 책

import re
import os

def clean_text(filename):
    if not os.path.exists(filename):
        print(f"[경고] 파일이 존재하지 않음: {filename}")
        return

    with open(filename, 'r', encoding='utf-8') as file:
        book_text = file.read()

    # 줄바꿈을 빈칸으로 변경
    cleaned_text = re.sub(r'\n+', ' ', book_text)
    # 여러 빈칸을 하나의 빈칸으로 변경
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    print('cleaned_' + filename, len(cleaned_text), 'characters')

    with open('cleaned_' + filename, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

# # 사용할 파일 리스트
# filenames_list = ['./LLM_Data/HarryPotter2.txt']

# for filename in filenames_list:
