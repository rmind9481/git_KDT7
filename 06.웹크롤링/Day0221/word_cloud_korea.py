# 필요한 라이브러리 임포트
from wordcloud import WordCloud  # WordCloud 생성을 위한 라이브러리
from konlpy.tag import Okt  # 한국어 형태소 분석을 위한 라이브러리
from collections import Counter  # 단어 빈도 수를 세기 위한 라이브러리
import matplotlib.pyplot as plt  # 데이터 시각화를 위한 라이브러리
import platform  # 운영체제 정보를 얻기 위한 라이브러리
import numpy as np  # 수치 계산을 위한 라이브러리
from PIL import Image  # 이미지 처리를 위한 라이브러리
import koreanize_matplotlib  # matplotlib에서 한글을 지원하기 위한 라이브러리

# 텍스트 파일을 읽어들임
text = open('./Data/test.txt', encoding='utf-8').read()  # 'test.txt' 파일을 UTF-8 인코딩으로 읽음

# Okt 객체 생성 (Open Korean Text)
okt = Okt()  # 한국어 형태소 분석을 위한 Okt 객체 생성

# 형태소 분석 결과를 저장할 리스트 초기화
sentences_tag = []  # 형태소 분석 결과를 저장할 리스트
sentences_tag = okt.pos(text)  # 텍스트의 형태소를 분석하여 품사 태깅

# 명사와 형용사를 저장할 리스트 초기화
noun_adj_list = []  # 명사와 형용사를 저장할 리스트

# 형태소 분석 결과에서 명사(Noun)와 형용사(Adjective)만 추출
for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:  # 태그가 명사 또는 형용사인 경우
        noun_adj_list.append(word)  # 해당 단어를 리스트에 추가

# 추출된 명사와 형용사 출력
print(noun_adj_list)

# 가장 많이 나온 단어부터 50개를 저장
counts = Counter(noun_adj_list)  # 명사와 형용사의 빈도 수를 세기
tags = counts.most_common(50)  # 가장 많이 나온 50개의 단어와 그 빈도 수를 저장

# 빈도 수가 높은 단어 출력
print(tags)

# 한글 폰트를 설정하기 위한 경로 지정
if platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'  # Windows의 경우 Malgun Gothic 폰트 경로
elif platform.system() == 'Darwin':  # Mac OS의 경우
    path = r'/System/Library/Fonts/AppleGothic'  # Apple Gothic 폰트 경로
else:
    path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'  # Linux의 경우 Nanum Myeongjo 폰트 경로

# 워드클라우드 생성을 위한 마스크 이미지 로드
img_mask = np.array(Image.open('./Data/cloud.png'))  # 마스크 이미지 파일을 numpy 배열로 변환

# 워드클라우드 객체 생성
wc = WordCloud(font_path=path,  # 한글 폰트 경로
               width=400,  # 이미지 너비
               height=400,  # 이미지 높이
               background_color="white",  # 배경 색상
               max_font_size=200,  # 최대 글자 크기
               repeat=True,  # 글자 반복 여부
               colormap='inferno',  # 색상 맵
               mask=img_mask)  # 마스크 이미지 적용

# 단어 빈도 수로부터 워드클라우드 생성
cloud = wc.generate_from_frequencies(dict(tags))  # 빈도 수를 딕셔너리 형태로 변환하여 워드클라우드 생성

# 생성된 워드클라우드를 test.jpg로 저장 (주석 처리됨)
# cloud.to_file('test.jpg')

# 워드클라우드 시각화
plt.figure(figsize=(10, 8))  # 그림 크기 설정
plt.axis('off')  # 축을 숨김
plt.imshow(cloud)  # 생성된 워드클라우드 이미지를 표시
plt.show()  # 이미지를 화면에 출력
