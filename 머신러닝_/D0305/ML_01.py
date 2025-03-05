import  sklearn

#print(sklearn.__version__)

# 첫번째 머신러닝 만들어보기 - 분꽃 품종 예측하기

# 사이킷런 에서 자체적으로 제공하는 데이트 세트 생성하는 모듈
from sklearn.datasets import load_iris
# 학습데이터와 검증 데이터, 예측 데이터로 데이터를 분리, 최적의 하이퍼 파라미터로 평가하기 위한 모듈
from sklearn.tree import DecisionTreeClassifier

# # 하이퍼 파라미터란 머신러닝 알고리즘 별 최적의 학습을 위해 직접 입력하는 파라미터들을 통칭

from sklearn.model_selection import train_test_split

# load_iris()를 이용하여 Ml 알고리즘은 의사 결정 트리 (Decision Tree) 알고리즘

import pandas as pd

# 붓꽃데이터 세트를 로딩
iris = load_iris()

# iris.data 는 Iris 데이터 세트에서 피처(feature)만으로 된 데이터를 numpy 로 가지고 있다.

iris_data = iris.data

# iris.target 은 붓꽃 데이터 세트에서 레이블(결정값 ) 데이터를 numpy 로 가지고있다.

iris_label = iris.target
print('iris target 값', iris_label)
print('iris target 명', iris.target_names)


# 붓꽃 데이터 세트를 자세히 보기 위해 DataFrame 으로 변환

iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
iris_df['label'] = iris.target
print(iris_df.head(3))

print(iris_df.info)

# 학습용 데이터와 테스트용 데이터 분리

# 학습용 데이터 와 테스트용 데이터는 반드시 분리해야된다.

# 학습데이터로 학습된 모델이 얼마나 뛰어난 성능을 가지는 지 평가하려면 테스트 세트가 필요
# train_test_split() API 를 제공

# train_size = 0.2 로 입력 파라미터를 설정하면 전체 데이터중 테스트데이터가 20% 학습데이터가 80% 로 데이터를 분할

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, train_size=0.2, random_state=11)

# 의사 결정 트리 사용 학습과 예측 수행
# 사이킷런의 의사결정 트리 클래스 => DecisionTreeClassfier 를 객체로 생성

dt_clf = DecisionTreeClassifier(random_state=11)

# 학습 수행
dt_clf.fit(X_train,y_train)

# 학습이 완료된 decisionTreeClassifier 객체에서 테스트 데이터 세트로 예측 수행


pred = dt_clf.predict(X_test)

# 사이킷런은 정확도 측정을 위해 accuracy_score() 함수를 제공
# accuracy_score() 첫번째 파라미터로 실제 레이블 데이터세트, 두번째 파라미터로 예측 레이블 데이터세트

from sklearn.metrics import accuracy_score
print('예측 정확도 :{0:.4f}'.format(accuracy_score(y_test,pred)))

# 분꽃 데이터 세트로 분류를 예측한 프로세스를 정리하면
# 1. 데이터 세트분리 : 데이터를 학습 데이터와 테스트 데이터로 분리
# 2. 모델 학습 : 학습 데이터를 기반으로 ML 알고리즘을 적용해 모델을 학습
# 3. 예측 수행 : 학습된 ML 모델을 이용해 테스트 데이터의 분류(즉, 붓꽃 종류)를 예측
# 4. 평가 : 이렇게 예측된 결괏값과 테스트 데이터의 실제 결괏값을 비교해 ML 모델 성능을 평가


