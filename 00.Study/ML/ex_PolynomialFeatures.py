import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 입력 데이터
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 6, 10, 18, 26])  # y = 2x + x²

# 다항 특성 변환 (2차)
poly = PolynomialFeatures(degree=2)#
X_poly = poly.fit_transform(X)

# 다중 회귀 모델 학습
model = LinearRegression()
model.fit(X_poly, y)

# 가중치 출력
print("가중치 (coef_):", model.coef_)
print("절편 (intercept_):", model.intercept_)

#StandardScaler 적용 후 학습하는 경우

from sklearn.preprocessing import StandardScaler

# 데이터 표준화
scaler = StandardScaler()
X_poly_scaled = scaler.fit_transform(X_poly)

# 다중 회귀 모델 학습
model.fit(X_poly_scaled, y)

# 가중치 출력
print("가중치 (coef_):", model.coef_)
print("절편 (intercept_):", model.intercept_)
