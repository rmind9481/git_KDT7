# --------------------------------------------------------------------------------
# Package(패키지)
# - 동일 카테고리에 여러 개의 모듈을 묶어 둔것
# - 접근 : 패키지명.모듈명
# - 사용법: import 패키지명.모듈명
# --------------------------------------------------------------------------------

# 모듈 로딩

# import urllib
import urllib.request as request

# --------------------------------------------------------------------
# 기능 코드
# --------------------------------------------------------------------

request.urlopen("http://www.google.co.kr")
LOGO_URL = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
request.urlretrieve(LOGO_URL,'logo.png' )
