import urllib.request  # URL 요청을 보내고 데이터를 가져오는 모듈
import datetime  # 날짜 및 시간 관련 기능을 제공하는 모듈
import json  # JSON 데이터를 처리하기 위한 모듈
import pandas as pd  # 데이터프레임을 사용하기 위한 라이브러리


def get_request_url(url):
    """ 네이버 검색 API 요청을 보내고 응답을 반환하는 함수 """
    client_id = "pNcRoroL4LkNMQ37AVVC"  # 네이버 API 클라이언트 ID
    client_secret = "oAskDsJSnm"  # 네이버 API 클라이언트 시크릿 키
    
    req = urllib.request.Request(url)  # 요청 객체 생성
    req.add_header('X-Naver-Client-Id', client_id)  # 클라이언트 ID 추가
    req.add_header('X-Naver-Client-Secret', client_secret)  # 클라이언트 시크릿 추가
    
    try:
        response = urllib.request.urlopen(req)  # API 요청 보내기
        if response.getcode() == 200:  # 응답 코드가 200(정상)인 경우
            return response.read().decode('utf-8')  # 응답 데이터 디코딩 후 반환
    except Exception as e:
        print(e)  # 오류 메시지 출력
        print(f'Error for URL : {url}')  # 오류 발생 URL 출력


def get_naver_search(node, search_text, start, display):
    """ 네이버 검색 API를 호출하여 JSON 형식의 데이터를 반환하는 함수 """
    base = "https://openapi.naver.com/v1/search"  # 기본 API URL
    node = f"/{node}.json"  # 검색 대상 (예: 뉴스, 블로그 등)
    query_string = f"{urllib.parse.quote(search_text)}"  # 검색어 인코딩
    
    # 요청 파라미터 설정
    parameters = f"?query={query_string}&start={start}&display={display}"
    url = base + node + parameters  # 최종 API URL 생성
    
    response = get_request_url(url)  # API 호출 및 응답 데이터 반환
    
    if response is None:
        return None  # 응답이 없는 경우 None 반환
    else:
        return json.loads(response)  # JSON 문자열을 Python 객체로 변환 후 반환


def get_post_data(post, json_result_list, cnt):
    """ 검색된 뉴스 데이터를 추출하여 리스트에 추가하는 함수 """
    title = post['title']  # 뉴스 제목
    description = post['description']  # 뉴스 요약
    org_link = post['originallink']  # 원본 기사 링크
    link = post['link']  # 네이버 뉴스 링크
    
    # 날짜 형식 변환 (API에서 제공하는 날짜 문자열을 가독성 있는 형식으로 변경)
    pdate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pdate = pdate.strftime('%Y-%m-%d %H:%M:%S')
    
    # 검색된 뉴스 정보를 콘솔에 출력
    print(f"[{cnt}]", end=" ")
    print(title, end=": ")
    print(pdate, end=" ")
    print(link)
    
    # 데이터를 리스트에 추가 (CSV 저장을 위해 사용)
    json_result_list.append([cnt, pdate, title, description, org_link, link])


def main():
    """ 메인 실행 함수 """
    node = 'news'  # 검색 대상 설정 (예: 뉴스 검색)
    search_text = '인공지능'  # 검색할 키워드 설정 (예: 사용자가 입력하는 방식도 가능)
    cnt = 0  # 출력 데이터 개수를 세는 변수

    json_result_list = []  # 검색 결과를 저장할 리스트
    
    json_response = get_naver_search(node, search_text, 1, 100)  # 검색 API 호출 (최대 100개 조회)
    
    # 검색 결과가 있고, display 값이 0이 아닐 경우 반복 실행
    while (json_response is not None) and (json_response['display'] != 0):
        for post in json_response['items']:
            cnt += 1  # 검색 결과 개수 증가
            get_post_data(post, json_result_list, cnt)  # 검색 결과 데이터 처리
        
        # 다음 페이지의 검색 결과를 가져오기 위해 start 값 갱신
        start = json_response['start'] + json_response['display']
        json_response = get_naver_search(node, search_text, start, 100)

    print(f'전체 검색 수: {cnt}')  # 총 검색된 기사 개수 출력
    
    # 검색 결과를 CSV 파일로 저장
    columns = ['count', 'date', 'title', 'description', 'org_link', 'link']  # 컬럼명 설정
    result_df = pd.DataFrame(json_result_list, columns=columns)  # 데이터프레임 생성
    result_df.to_csv(f'{search_text}_naver_{node}.csv', index=False, encoding='utf-8')  # CSV 파일 저장


# 프로그램 실행 (메인 함수 호출)
if __name__ == '__main__':
    main()
           