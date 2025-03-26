import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


# X 데이터 (입력값)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)

# Y 데이터 (출력값)
y = np.array([2, 6, 12, 20, 30, 42, 56, 72, 90, 110])  # y = x^2 + x

# 선형 회귀 모델 학습
linear_model = LinearRegression()
linear_model.fit(X, y)
y_pred_linear = linear_model.predict(X)

# 다항 회귀 모델 학습 (차수=2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_pred_poly = poly_model.predict(X_poly)

# 그래프 그리기
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred_linear, label="Linear Regression", linestyle="dashed")
plt.plot(X, y_pred_poly, label="Polynomial Regression (degree=2)", color="red")
plt.legend()
plt.xlabel("X (시간)")
plt.ylabel("Y (성장)")
plt.title("Linear vs Polynomial Regression")
plt.show()


from sklearn.model_selection import cross_val_score

# 차수별 성능 비교
# 5. 최적의 차수 찾기 (K-Fold 교차 검증 활용)
for d in range(1, 6):  # 1차부터 5차까지 비교
    poly = PolynomialFeatures(degree=d)
    X_poly = poly.fit_transform(X)
    
    model = LinearRegression()
    scores = cross_val_score(model, X_poly, y, cv=5, scoring='r2')
    
    print(f"Degree {d}: 평균 R² Score = {np.mean(scores):.4f}")


from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import MinMaxScaler
import numpy as np

X = np.array([[10], [20], [30], [40], [50]])
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
print(X,X_scaled)

