import numpy as np
from sklearn.preprocessing import StandardScaler, RobustScaler

# 이상치가 포함된 데이터
X = np.array([[50], [55], [60], [65], [70], [1000]])

# StandardScaler 적용
scaler = StandardScaler()
X_standard_scaled = scaler.fit_transform(X)

# RobustScaler 적용 # 중앙값
# RobustScaler는 평균(mean)과 표준편차(std)를 사용하지 않기 때문에 이상치 영향을 줄일 수 있음
# 하지만 이상치가 극단적으로 크면, 변환된 값도 여전히 상대적으로 큰 값이 될 수 있음
robust_scaler = RobustScaler()
X_robust_scaled = robust_scaler.fit_transform(X)

# 결과 출력
print("StandardScaler 변환 결과:\n", X_standard_scaled)
print("RobustScaler 변환 결과:\n", X_robust_scaled)

# 1️ **선형 회귀(Linear Regression)**는 먼저 분석하는 기본 모델로 사용됨
# 2️ 선형 회귀가 적절하지 않다면 **다항 회귀(Polynomial Regression)**를 적용하여 곡선 형태의 데이터를 학습
# 3️ 다항 회귀는 입력 변수를 증가시키는 과정이므로, 다중 회귀(Multiple Regression)와 연결됨
# 4️ 즉, 다항 회귀 자체가 다중 회귀로 변환된 형태로 사용됨 