# -------------------------------------------------------------
# 함수기능 : DataFrame 의 컬럼별 고유값 개수와 고유값 출력
# 함수이름 : print_Unique_Value
# 매개변수 : df_columns
# 반 환 값 : 없음
# -------------------------------------------------------------

def print_Unique_Value(df):
    for col in df.columns:
        print(f'\n\n[{col} 컬럼의 고유값]=========')
        print(f"고유값 갯수 : {df[col].nunique()}")
        print(f"{df[col].unique()}")
