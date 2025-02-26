import urllib.request  # URL 요청을 보내고 데이터를 가져오는 모듈
import datetime  # 날짜 및 시간 관련 기능을 제공하는 모듈
import json  # JSON 데이터를 처리하기 위한 모듈

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
    
    parameters = (f"?query={query_string}&start={start}&display={display}")  # 요청 파라미터 설정
    url = base + node + parameters  # 최종 API URL 생성
    response = get_request_url(url)  # API 호출 및 응답 데이터 반환
    
    if response is None:
        return None  # 응답이 없는 경우 None 반환
    else:
        return json.loads(response)  # JSON 문자열을 Python 객체로 변환 후 반환

def main():
    """ 메인 실행 함수 """
    node = 'news'  # 검색 대상 설정 (예: 뉴스 검색)
    search_text = input('검색어를 입력하세요: ')  # 사용자 입력을 통해 검색어 설정
    
    cnt = 0  # 출력 데이터 개수를 세는 변수
    json_response = get_naver_search(node, search_text, 1, 100)  # 검색 API 호출
    
    if (json_response is not None) and (json_response['display'] != 0):  # 검색 결과가 있는 경우
        for post in json_response['items']:  # 검색 결과 목록 반복 처리
            cnt += 1  # 결과 개수 증가
            print(f"[{cnt}]", end=" ")
            print(post['title'])  # 뉴스 제목 출력
            print(post['description'])  # 뉴스 요약 출력
            print(post['originallink'])  # 원본 링크 출력
            print(post['link'])  # 네이버 뉴스 링크 출력
            print(post['pubDate'])  # 뉴스 게시 날짜 출력

if __name__ == '__main__':
    main()  # 메인 함수 실행