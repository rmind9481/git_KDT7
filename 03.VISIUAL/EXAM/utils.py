## -----------------------------------------------------
## 함수 기능 : DataFrame의 기본정보 읽기
## 함수 이름 : print_DF_Information(df)
## 매개 변수 : df
## 반 환  값 : 없음
## -----------------------------------------------------
def print_DF_Information(df, dfName):

    print(f"{dfName} 의 요약정보 =====\n\n")
    df.info()
    print(f"{dfName} 의 앞줄 2개 =====\n{df.head(2)}")
    print(f"{dfName} 의 뒷줄 2개 =====\n{df.tail(2)}")
    print(f"{dfName} 의 데이터 타입 =====\n{df.dtypes}")
    print(f"{dfName} 의 통계치 =====\n{df.describe()}")

def Check_cloums_index(df, dfname):
    print(f"{dfname}의 columns =====\n{df.columns}")
    print(f"{dfname}의 Index =====\n{df.index}")
    print(f"{dfname}의 values =====\n{df.values}")
    print(f"{dfname}의 Shape =====\n{df.shape}")
    

## -----------------------------------------------------
## 함수 기능 : DataFrame의 컬럼별 고유값 개수와 고유값 출력
## 함수 이름 : printUniqueValue
## 매개 변수 : df
## 반 환  값 : 없음
## -----------------------------------------------------
def printUniqueValue(df):
    for col in df.columns:
        print(f'\n[{col}컬럼의 고유값]=====')
        print('갯수 : ', df[col].nunique() )
        print( df[col].unique())