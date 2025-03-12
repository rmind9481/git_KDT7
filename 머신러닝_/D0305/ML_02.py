# 사이킷런의 기반 프레임 워크 익히기

# Estimator 이해 및 fit(),predict() 메서드
# 사이킷런은 ML 모델 학습을 위해서 fit() 를
# 학습된 모델의 예측을 위해 predict() 메서드를 제공
# 분류 알고리즘 을 구현한 클래스를 Classifiter 
# 회귀 알고리즘을 구현한 클래스를 Regressor

# Classifiter 와 Regressorr 를 합쳐서 Estimator 클래스
# 
# cross_val_score() evaluation 함수, GridSearchCV와 같은 하이퍼 파라미터 튜닝을 지원하는 클래스의 경우
# Estimator 를 인자로 받는다.

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np
from sklearn.model_selection import KFold

dt_clf = DecisionTreeClassifier()
iris_data = load_iris()
keys = iris_data.keys()
print(f'붓꽃데이터 세트의 키들 : {keys}')
X_train, X_text, y_train, y_test, = train_test_split(iris_data.data, iris_data.target, \
														test_size=0.3, random_state=121)
print('\nfeature_names 의 type:', type(iris_data.feature_names))
print('feature_names 의 shape:', len(iris_data.feature_names))
print(iris_data.feature_names)

print('\ntarget_names 의 type: ', type(iris_data.target_names))

print('target_names 의 shape:', len(iris_data.target_names))
print(iris_data.target_names)

print('\ntarget 의 type:', type(iris_data.target))
print('target 의 shape:', iris_data.target)
print(iris_data.target)


# Model Selection 모듈소개

iris = load_iris()
dt_clf.fit(X_train, y_train)
train_data = iris.data
train_label = iris.target
dt_clf.fit(train_data, train_label)

# 학습 데이터 세트로 예측 수행
pred = dt_clf.predict(train_data)
print('예측 정확도 :', (accuracy_score(train_label,pred)))


# 정확도 100% 입니다. 
# 데이터 세트는 학습을 수행한 학습용 데이터  



X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.3, random_state=121)


# 학습/테스트 데이터 세트분리

dt_clf.fit(X_train, y_train)
pred = dt_clf.predict(X_text)
print('예측 정확도 : {0:4f}'.format(accuracy_score(y_test,pred)))

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['label'] = iris.target
iris_df['label'].value_counts()

print(iris_df['label'])


# 교차 검증  K폴드 교차 검증
# K 폴드 교차 검증으 ㄴ가장 보편적으로 사용되는 교차 검증 기법
# K번 만큼 각 폴트 세트에서 학습과 검증
 


iris = load_iris()
features = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=156)

# 5개 의 폴드 세트로 분리하는 KFold 객체와 폴드 세트별 정확도를 담을 리스트 객체 생성
kfold = KFold(n_splits=5)
cv_accuracy = []

print('붓꽃 데이터 세트 :',features.shape[0])

# KFold 객체의 split()를 호출하면 폴드별, 학습용, 검증용 테스트의 로우 인덱스를 array 로 반환

n_iter = 0

for train_index, test_index in kfold.split(features):
	# kfold.split() 으로 반환된 인덱스를 이용해 학습용, 검증용 테스트 데이터 추출
	X_train, X_test  = features[train_index], features[test_index]
	y_train, y_test = label[train_index],label[test_index]

	# 학습 및 예측
	dt_clf.fit(X_train, y_train)
	pred = dt_clf.predict(X_test)
	n_iter +=1
	# 반복시 마다 정확도 측정
	accuracy = np.round(accuracy_score(y_test,pred),4)
	train_size = X_train.shape[0]
	test_size = X_test.shape[0]
	print('\n#{0} 교차 검증 정확도 : {1}, 학습 데이터 크기:  {2}, 검증 데이터 크기: {3}'.format(n_iter,accuracy, train_size,test_size))

	cv_accuracy.append(accuracy)

# 개별 iteration 별 정확도를 합하여 평균 정확도 계산
print('\n## 평균 검증 정확도:', np.mean(cv_accuracy))

