# 1.데이터준비
# - 데이터셋 구하기
# - 데이터 전처리 (정수 인코딩, 원핫 인코딩, 정규화)

# 2.데이터 로더 생성
# - Dataset 클래스 만들기 
# - DataLoader 사용해 배치단위로 데이터 불러오기

# 3.모델 설계
# - 입력층 -> 은닉층 -> 출력층 구조 

# 4. 손실 함수 와 옵티마이저 설정
# - CrossEntroyLoss 사용 (다중 분류에서 필수)
# - 옵티마이저는 SGC, Adam 등 사용

# 5. 학습(Training)
# - 순전파 -> 손실계산 -> 역전파 -> 파라미터 업데이트

# 6. 평가 (Validation/Test)
# - 정확도, Loss 확인


# 예측
# -새 데이터에 대해 예측

# 시각화
# -Loss 와 Accuracy 변화 그래프

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch 
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 불러오기
data = r'C:\Users\rmind\Desktop\git_KDT7\10.DL\Data\iris.csv'
iris_DF =  pd.read_csv(data)


# 데이터 확인
#print(iris_DF.info())

# 데이터 전처리
#print(iris_DF.variety.unique())
iris_DF.variety=iris_DF.variety.replace({'Setosa':0, 'Versicolor':1, 'Virginica':2})

iris_DF.variety.astype('int')
#print(iris_DF.info())



feature = iris_DF.iloc[:,:-1]
print(feature.head())
target = iris_DF.iloc[:,-1]
print(target.head())

# 학습용 테스트용 분리

X_train, X_test, y_train, y_test = train_test_split(feature,target, test_size=0.2,random_state=42)


class DF_Dataset(Dataset):
    def __init__(self,feature, target):
        super().__init__()
        self.feature = torch.tensor(feature.values, dtype=torch.float32)
        self.target = torch.tensor(target.values, dtype=torch.long)
        
        

    def __len__(self):
        return len(self.feature)

    def __getitem__(self,idx):
        return self.feature[idx], self.target[idx]
    

# Dataset 객체생성
train_DS = DF_Dataset(X_train,y_train)
test_DS = DF_Dataset(X_test,y_test)

# DataLoader 생성

train_Loader = DataLoader(dataset=train_DS,batch_size= 16, shuffle=True ) 
test_Loader = DataLoader(dataset=test_DS,batch_size= 16) 

# 모델설계
# 다중 분류
# 입력값 4 
# 은닉층 1
# 출력 3
class IrisModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.in_layer = nn.Linear(4,16)
        self.hd_layer1 = nn.Linear(16,8)
        self.out_layer = nn.Linear(8,3)

    def forward(self, out):
        out = torch.relu(self.in_layer(out))
        out = torch.relu(self.hd_layer1(out))
        out = self.out_layer(out)

        return out

# 모델 생성
iris_model = IrisModel()
# 손실함수와 옵티마이저 설정

# 다중분류에서 주로 쓰임
criterion = nn.CrossEntropyLoss() 
lr = 0.01
optimizer = optim.Adam(iris_model.parameters(),lr=lr)

# 학습

num_epochs = 50
train_loss_history = []

for epoch in range(num_epochs):
    iris_model.train()
    LOSS = 0.0

    for inputs, labels in train_Loader:
        #print(inputs,labels)   
        outputs = iris_model(inputs)
        # 예측값 / 정답  오차 비교
        loss = criterion(outputs, labels)

        # 역전파
        # 미분 초기화
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        LOSS += loss.item()
    avg_loss = LOSS/ len(train_Loader)
    train_loss_history.append(avg_loss)
    print(f'Epoch {epoch+1}, Loss:{avg_loss:.5f}')



# 평가
iris_model.eval()

correct = 0
total =0

with torch.no_grad():
    for inputs, labels in test_Loader:
        outputs = iris_model(inputs)
        _, pred = torch.max(outputs,1)
        total += labels.size(0)
        correct += (pred == labels).sum().item()


accuarcy = correct/total
print(f'테스트 정확도 :{accuarcy:.2f}')

# 손실 함수 변화 시각화

plt.plot(train_loss_history, marker='o')
plt.title('학습 Loss 변화')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid()
plt.show()


