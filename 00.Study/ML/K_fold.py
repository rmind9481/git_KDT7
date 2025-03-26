import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split , KFold 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

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


# K_Flold 교차 검증 설정
K_Fold = KFold(n_splits=4, shuffle=True, random_state=42)


# K_Fold 교차 검증 

mse_scores = [] # 각 fold 의 mse 저장

for train_index, val_index in K_Fold.split(X_train_scaled):
	# 훈련데이터 와 검증 데이터 나누기
	X_train_kf, X_val_kf = X_train_scaled[train_index], X_train_scaled[val_index]
	y_train_kf, y_val_kf = y_train[train_index], y_train[val_index]


	# 다중 회귀 모델 학습
	model = LinearRegression()
	model.fit(X_train_kf, y_train_kf)
	# 검증 데이터로 예측

	y_val_pred = model.predict(X_val_kf)

	# mse 계산
	mse = mean_squared_error(y_val_kf, y_val_pred)
	mse_scores.append(mse)

# 가중치와 절편 출력
print("가중치 (coef_):", model.coef_)
print("절편 (intercept_):", model.intercept_)


# K-Fold 결과 출력
print(f"K-Fold 교차 검증에서 각 fold의 MSE: {mse_scores}")
print(f"K-Fold 교차 검증에서 평균 MSE: {np.mean(mse_scores)}")

# 전체 훈련 데이터로 학습한 후 테스트 데이터로 예측
model.fit(X_train_scaled, y_train)
y_test_pred = model.predict(X_test_scaled)

# 테스트 데이터의 MSE 출력
test_mse = mean_squared_error(y_test, y_test_pred)
print(f"테스트 데이터의 MSE: {test_mse}")