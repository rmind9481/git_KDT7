import os  # 운영 체제와 상호작용하기 위한 모듈
import sys  # 시스템 관련 기능을 제공하는 모듈
import urllib.request  # URL을 열고 데이터를 가져오는 기능을 제공하는 모듈

# 네이버 검색 API 사용을 위한 클라이언트 ID와 시크릿 키 설정
client_id = "pNcRoroL4LkNMQ37AVVC"  # 네이버 API 클라이언트 ID
client_secret = "oAskDsJSnm"  # 네이버 API 클라이언트 시크릿 키

# 검색할 키워드 설정 및 URL 인코딩 (특수 문자 포함 가능하도록 변환)
encText = urllib.parse.quote("빅데이터")  # "빅데이터"라는 키워드를 검색하도록 설정

# 네이버 검색 API 블로그 검색 URL 생성 (JSON 형식 응답 요청)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # JSON 결과 반환
# XML 결과를 원할 경우 아래 URL을 사용할 수도 있음
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText  # XML 결과 반환

# HTTP 요청 객체 생성
request = urllib.request.Request(url)

# 요청 헤더에 네이버 API 인증 정보를 추가 (클라이언트 ID 및 시크릿 키)
request.add_header("X-Naver-Client-Id", client_id)  # 클라이언트 ID 설정
request.add_header("X-Naver-Client-Secret", client_secret)  # 클라이언트 시크릿 설정

# API 요청을 보내고 응답을 받음
response = urllib.request.urlopen(request)  # API 호출 및 응답 저장
rescode = response.getcode()  # HTTP 응답 코드 확인 (200: 정상 응답)

# 응답 코드가 200(정상)일 경우 결과 출력
if rescode == 200:
    response_body = response.read()  # 응답 데이터 읽기
    print(response_body.decode('utf-8'))  # UTF-8 디코딩 후 출력 (JSON 형식 문자열)
else:
    # 오류 발생 시, HTTP 응답 코드 출력
    print("Error Code:" + str(rescode))
