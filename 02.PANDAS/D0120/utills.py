# ----------------------------------------------------------------
#  Pandas 데이터 관련 사용자 정의 함수들
# ----------------------------------------------------------------

# ---------------------------------------------------------------------------

# 함수기능 : 데이터프레임 속성 출력
# 함수이름 : print_attribute
# 매개변수 : df , dfname
# 반 환 값 : 없음
# ---------------------------------------------------------------------------

def print_attribute(df, dfname):
    print('데이터 이름',dfname)
    # 타입
    print('타입 출력',df.dtypes)
    # 컬럼 출력
    print('컬럼 출력',df.columns)
    # 인덱스 출력
    print('인덱스 출력',df.index)
    # 차원 출력
    print('차원 출력',df.ndim)
    # (행,열) 출력
    print('(행,열) 출력',df.shape)
    # 데이터 출력
    print('데이터출력\n', df.values) 

# ---------------------------------------------------------------------------

# 함수 기능 : 데이터프레임의 요약정보, 실제 데이터, 통계치
# 함수 이름 : summary
# 매개 변수 : df - 데이터프레임 객체, dfname - 데이터프레임 이름
# 함수 결과 : 없음
# ---------------------------------------------------------------------------

def summary(df, dfname):
    # 요약정보 출력
    print(dfname)
    df.info()
    # 실제 데이터 일부 출력
    print(df.head(2),df.tail(2), sep="\n\n")
    # 통계치 출력
    print(df.describe())