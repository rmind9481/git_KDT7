
"""
FILENAME    : utils.py
DESCIRPTION : 데이터 분석에 자주 사용되는 기능의 함수들 관련 모듈
DATA        : 2025.01.15
HISTORY     : WRITER             DATA               DESC
                SO              2025.01.05      print_info() 추가
                HONG            2025.01.15      
"""



# ----------------------------------------------------
#   함수기능 : 개발 정보 출력기능
#   함수이름 : print_info()
#   매개변수 : 없음
#   리 턴 값 : 없음
#   
# ----------------------------------------------------

def print_info():
    print("회사명 : KNU")
    print("연락처 : 053-0000-0000")
    print("버 전  : v1.0")
    print("담당자 : 홍길동")

# 함수 호출 /사용

# __name__ 

print('utils.py',__name__)

if __name__ == "__main__":
    print_info()