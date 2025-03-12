import sklearn
import pandas as pd           
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split



print(sklearn.__version__)

# 붓꽃 데이터 세트를 로딩
iris = load_iris()

# iris.data 는 iris 데이터 세트에서 피처 만으로 된 데이터를 numpy 로 가지고 있다.
iris_data = iris.data

# iris.target 은 붓꽃 데이터 세트에서 레이블 데이터를 numpy 로 가지고 있다.

iris_label = iris.target


# iris.target 은 붓꽃데이터 세트에서 레이블 (결정 값) 