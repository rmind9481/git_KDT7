# ----------------------------------------------------------------
#   DataFrame 에서 행 선택/추출 => 가로 한줄 선택
# ----------------------------------------------------------------
# [1] 모듈로딩
# ----------------------------------------------------------------

import pandas as pd

# ----------------------------------------------------------------
# [2] 데이터 준비 
# ----------------------------------------------------------------

FILENAME = r"C:\Users\KDP-17\Desktop\KDT_7\02.PANDAS\DATA\iris.csv"

irisDF = pd.read_csv(FILENAME)
print(irisDF)

# ---------------------------------------------------------------
# [3] 데이터 확인 => 속성: index, columns, values, dtypes, shape, ndim
# ---------------------------------------------------------------
#  - 속성 읽기 : 변수명, 속성명

print(f'index{irisDF.index}')
print(f'columns{irisDF.columns}')
print(f'dtypes{irisDF.dtypes}')
print(f'shape{irisDF.shape}')
print(f'ndim{irisDF.ndim}')


# -DataFrame 기본 정보 출력 메서드 => 객체변수명.info()

irisDF.info()

# -DataFrame 컬럼별 수치형 컬럼에 대한 통계치 계싼 메서드 > 객체변수명.desc()

print(irisDF.describe())

# -DataFrame 모든 컬럼에 대한 통계치 계산 메서드 => 객체변수명.describe(include='all')
print(irisDF.describe(include='all'))


# ---------------------------------------------------------------
# [4] 행 선택/추출
#       => 객체변수명.loc[행인덱스]
#       => 객체변수명.iloc[행인덱스-정수]
# ---------------------------------------------------------------
#  - 속성 읽기 : 변수명, 속성명

irisDF.iloc[0]
print('0번행 =>',irisDF.iloc[0])
print('0번행 타입 =>',type(irisDF.iloc[0]))

# [4-2] 여러개 행 선택
print('0번, 2번행 =>', irisDF.iloc[[0,2]])
print('0번, 2번행 =>', type(irisDF.iloc[[0,2]]))


# [0:6] 0<= ~ <6
print('0번~5번행 =>', type(irisDF.iloc[0:6]))

# [0:6:2] 0,2,4  
print('0번~5번행 =>', type(irisDF.iloc[0:6:2]))
print('0번~5번행 =>', type(irisDF.iloc[0:6:2]))


# [4-3]=> 행 인덱스 0번 행 부터 4번행까지 일부 변경

irisDF2=irisDF.rename(index={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five'})

print(irisDF2.index)

# 1개 행 선택
print(f'.iloc[0] => {irisDF2.iloc[0]}')
print(f'.iloc["zero"] => {irisDF2.loc["zero"]}')