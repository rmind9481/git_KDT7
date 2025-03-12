import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 랜덤 시드 고정
np.random.seed(42)

# 입력 변수 (X) : 기온(°C), 습도(%), 홍보비(만원)
X = np.array([[30, 70, 100], [25, 60, 50], [20, 50, 10], [35, 80, 200], [15, 40, 5]])
# 출력 변수 (y) : 매출(개)
y = np.array([200, 150, 50, 300, 30])

# 데이터를 훈련용과 테스트용으로 분리 (일관된 결과를 위해 random_state 설정)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터 표준화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 다중 회귀 모델 학습
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 가중치와 절편 출력
print("가중치 (coef_):", model.coef_)
print("절편 (intercept_):", model.intercept_)
