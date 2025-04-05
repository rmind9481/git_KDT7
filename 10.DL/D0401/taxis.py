import torch 
import torch.nn as nn
import pandas as pd
import numpy as np
import torch.nn.functional as F


# pickup	택시가 승객을 태운 시간(일반적으로 datetime 형식). 승차가 시작된 시점.
# dropoff	승객을 하차시킨 시간(일반적으로 datetime 형식). 택시 여행이 끝난 시점.

# passengers	택시에 탑승한 승객의 수. 택시 여행에 참여한 총 승객의 수.

# distance	택시가 이동한 거리(킬로미터 또는 마일 단위). 실제 이동한 거리를 나타냄.

# fare	택시 요금의 기본 요금. 택시 여행의 시작에 대한 요금.
# tip	승객이 택시 운전사에게 준 팁 금액.
# tolls	여행 중 발생한 유료 도로 이용 요금.

# total	총 요금. 기본 요금(fare), 팁(tip), 유료 도로 요금(tolls) 등을 포함한 전체 요금.

# color	택시의 색상.

# payment	지불 방법. 현금, 카드, 전자 지갑 등 다양한 방법으로 구분됨.

# pickup_zone	승차 지점이 속한 지역 또는 구역. 특정 지역 구분에 따라 값을 가짐.
# dropoff_zone	하차 지점이 속한 지역 또는 구역.

# pickup_borough	승차 지점이 속한 도시나 구. 예: Manhattan, Brooklyn 등.
# dropoff_borough	하차 지점이 속한 도시나 구. 예: Manhattan, Brooklyn 등.

FILE = '../Data/taxis.csv'

taxis_DF = pd.read_csv(FILE)
taxis_DF.info()
print(taxis_DF.head())
print(taxis_DF['pickup'])

# pickup / dropoff  시계열 타입으로 변화 => 택시 이용시간 체크
