import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# 입력 변수 (X) : 기온(°C), 습도(%), 홍보비(만원)
X = np.array([[30, 70, 100], [25, 60, 50], [20, 50, 10], [35, 80, 200], [15, 40, 5]])
# 출력 변수 (y) : 매출(개)
y = np.array([200, 150, 50, 300, 30])

# 다중 회귀 모델 학습 (StandardScaler 없이)
model = LinearRegression()
model.fit(X, y)

print("가중치 (coef_):", model.coef_)
print("절편 (intercept_):", model.intercept_)

#  StandardScaler 없이 학습하는 경우
# ➡ 홍보비(0.08)의 가중치가 매우 작음 → 홍보비의 크기가 크기 때문!
# ➡ 기온(2.0), 습도(1.5)보다 홍보비가 상대적으로 덜 중요한 변수로 판단됨



# 2 StandardScaler 적용 후 학습

# StandardScaler 적용
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 변환된 데이터 확인
print("변환전 X 데이터:\n", X)
print("변환된 X 데이터:\n", X_scaled)

# 다중 회귀 모델 학습 (표준화 적용 후)
model = LinearRegression()
model.fit(X_scaled, y)

print("가중치 (coef_):", model.coef_)
print("절편 (intercept_):", model.intercept_)
