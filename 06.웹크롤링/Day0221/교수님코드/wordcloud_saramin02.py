from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import quote
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import platform
import numpy as np
from PIL import Image

def get_sector_data(url, keyword, sector_list):
    '''
    사람인에서 특정 검색어에 대한 채용 공고를 크롤링하여 <div class="job_sector"> 안에 있는 직무 분야 텍스트를 추출
    추출한 직무 분야 데이터를 sector_list 리스트에 추가
    '''
    try:
        # HTTP 요청을 보낼 때 User-Agent를 설정하여 크롤링 차단을 방지
        urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(urlrequest)  # URL 요청 실행
        soup = BeautifulSoup(html, 'html.parser')  # BeautifulSoup을 사용하여 HTML 파싱
        
        # 채용 공고 아이템을 포함하는 div 태그 찾기
        job_items = soup.find_all('div', {'class': 'item_recruit'})
        
        # 각 채용 공고에서 직무 분야 추출
        for job in job_items:
            job_sectors = job.find('div', {'class': 'job_sector'})  # 직무 분야가 있는 div 찾기
            if job_sectors:
                sector_items = job_sectors.find_all('a', {'target': '_blank'})  # 직무별 링크 텍스트 추출
                for sector in sector_items:
                    sector_text = sector.text.replace('\n', '').strip()  # 텍스트 정리 (개행 문자 제거, 공백 제거)
                    sector_list.append(sector_text)  # 리스트에 추가
    except Exception as e:
        print(f'Error occurred: {e}')  # 오류 발생 시 출력

def make_wordcloud(word_list, stopwords, word_count):
    '''
    크롤링한 직무 분야 데이터를 이용해 워드 클라우드 생성
    특정 단어(stopwords 리스트에 포함된 단어)는 제외
    '''
    okt = Okt()  # Okt 형태소 분석기 객체 생성
    
    counts = Counter(word_list)  # 단어 빈도 계산
    tags = counts.most_common(word_count)  # 가장 많이 등장한 word_count개의 단어 선택
    tag_dict = dict(tags)  # 리스트를 딕셔너리로 변환
    
    # 제외할 단어(stopwords 리스트에 포함된 단어) 삭제
    for stopword in stopwords:
        if stopword in tag_dict:
            tag_dict.pop(stopword)
    
    print('-' * 80)
    print('tag_dict:', tag_dict)  # 최종적으로 사용할 단어 빈도 출력

    # OS별 폰트 설정 (워드 클라우드에서 한글 폰트 지원을 위해 필요)
    if platform.system() == 'Windows':
        path = r'c:\Windows\Fonts\malgun.ttf'  # Windows: 맑은 고딕
    elif platform.system() == 'Darwin':  # Mac OS
        path = r'/System/Library/Fonts/AppleGothic'  # Mac: 애플고딕
    else:
        path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'  # Linux: 나눔명조 (기본 폰트 경로)
    
    # 워드 클라우드 마스크 이미지 설정 (모양을 지정하기 위한 이미지)
    img_mask = np.array(Image.open('../Data/cloud.png'))
    
    # 워드 클라우드 생성 (백그라운드는 흰색, 글자 색상은 inferno 컬러맵 적용)
    wordcloud = WordCloud(
        font_path=path, width=800, height=600,
        background_color="white", max_font_size=200,
        repeat=True, colormap='inferno', mask=img_mask
    )
    
    cloud = wordcloud.generate_from_frequencies(tag_dict)  # 워드 클라우드 생성
    
    # 결과 출력
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

if __name__ == '__main__':
    keyword = '챗봇'  # 검색 키워드 설정
    sector_list = []  # 크롤링한 직무 분야를 저장할 리스트
    stopwords = [keyword, '챗봇']  # 워드 클라우드에서 제외할 단어 리스트
    
    search_word = quote(keyword)  # URL에서 사용할 검색어 인코딩

    # 1~9페이지까지 크롤링 실행
    for page in range(1, 10):
        url = f'https://www.saramin.co.kr/zf_user/search?' \
              f'search_area=main&search_done=y&search_optional_item=n&searchType=search&' \
              f'searchword={search_word}&recruitPage={page}'
        
        get_sector_data(url, keyword, sector_list)  # 크롤링 실행
        print(f'Page {page}: {sector_list}')
        print('-' * 90)
    
    print(f'Total sector_list length: {len(sector_list)}')  # 크롤링한 데이터 개수 출력
    
    make_wordcloud(sector_list, stopwords, 50)  # 워드 클라우드 생성
