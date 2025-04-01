# DNN 으로 구현
# Deep Neural Network

import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F

import torch.utils
import torch.utils.data
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader


# CPU 혹은 GPU 장치확인
# torch.cuda.is_available()은 시스템에 CUDA가 활성화된 GPU가 있는지 확인하는 함수
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

print(device)


transform = transforms.Compose(
    [transforms.ToTensor()]
    )
    
trainset = torchvision.datasets.FashionMNIST(root='./data', train=True, 
                                        download=True, transform=transform)
                                        
testset = torchvision.datasets.FashionMNIST(root='./data', train=False,
                                        download=True, transform=transform)




# torchvision.datasets 는 torch.utils.data.Dataset 의 하위 클래스로
# 다양한 데이터셋(CIFAR, COCO, MINIST< ImageNet 등)을 포함

# <torchvision.datasets 파라미터>
# root: FashionMNIST 데이터셋이 저장될 경로입니다. 지정한 경로가 없으면 새로 생성
# train = True 학습용 데이터셋을 다운
# download =True : 데이터셋이 저장될 경로에 데이서텟이 있는지 확인한후 없는 경우 다운
# transform = transform 입련된 이미지 데이터를 텐서 (0~1) 형태로 볍ㄴ경


#  fashion_mnist 데이터를 데이터로더에 전달
#  일정한 batch size로 묶어서 데이터로더(DataLoader) 를 만들어주는 코드


train_loader = torch.utils.data.DataLoader(trainset, batch_size=100, shuffle=True)

test_loader = torch.utils.data.DataLoader(testset, batch_size=100, shuffle=False)

# torch.utils.data.DataLoader() 를 사용하여 원하는 크기의 배치 단위로 데이터를 불러오거나,
# 순서가 무작위로 섞이도록 학습

#<DataLoader 파라미터>

# trainset : 데이터를 부러올 데이터셋을 지정
# batch_size : 데이터를 배치로 묶어줍니다. 100개 단위로 묶어준다.
# shuffle : 데이터를 불러올때마다 데이터를 섞어서 불러온다


# 분류에 사용될 클래스의 정의

# FashionMNIST 데이터셋으로 부터 랜덤으로 24개의 샘플 이미지와 라벨을 가져와서 시각화 하는 코드
# DataLoader 에서 shuffle = True 로 설정되어있기 때문에 매 Epoch 마다 데이터가 랜덤하게 섞인다.
# next(iter(train_loader)) 를 호출할때마다 다른 미니배치가 반환

# train_loader 에서 첫 번째 배치를 가져와 이미지와 라벨을 sample, labels 에 저장
samples, labels = next(iter(train_loader))

# 각 클래스의 이름을 숫자와 매칭하여 저장 (총10개)

classes = {0: 'T-Shirt', 1: 'Trouser', 2: 'Pullover', 3: 'Dress', 4: 'Coat', 5: 'Sandal', 6: 'Shirt', 7: 'Sneaker', 8: 'Bag', 9: 'Ankle_Boot'}

# 4행 6열 서브플롯 생성
fig, axs = plt.subplots(nrows=4, ncols=6, figsize=(16, 10))  # 서브플롯 생성

fig.suptitle("Fashion MNIST Dataset", fontsize=16)  # 전체 제목을 설정

for ax, image, label in zip(axs.flatten(), samples, labels):
    image = np.transpose(image.numpy(), (1, 2, 0))  # 차원 변환: (C, H, W) -> (H, W, C)
    
    ax.imshow(image, cmap='gray')  # 흑백 이미지로 출력
    ax.set_title(classes[label.item()], fontsize=12)  # label.item(): torch.Tensor 타입의 스칼라 값(정수)을 얻기 위해 사용
    ax.set_xticks([])  # x축 눈금을 숨김
    ax.set_yticks([])  # y축 눈금을 숨김

plt.tight_layout()  # 레이아웃 조정
plt.subplots_adjust(top=0.9)  # 서브플롯 간의 간격 조정 (전체 제목이 잘 보이도록)
plt.show()

# 심층 신경망 모델 (DNN) 생성

class Fashin_DNN(nn.Module):
	def __init__(self):
		super(Fashin_DNN, self).__init__()
		self.in_layer = nn.Linear(in_features=784, out_features=256)
		self.drop = nn.Dropout(0.25)
		self.hd_layer1 = nn.Linear(in_features=256, out_features=128)
		self.out_layer = nn.Linear(in_features=128, out_features=10)

	def forward(self, input_data):
		out = input_data.view(-1,784)
		out = F.relu(self.in_layer(out))
		out = self.drop(out)
		out = F.relu(self.hd_layer1(out))
		out = self.out_layer(out)
		return out
	
	# 클래스 torch.nn.Module 을 상속
	# __init__.() 은 객체가 갖는 속성 값을 초기화 하는 역활을 하며, 객체가 생성될때 자동으로 호출됩니다.
	# super(FasionDNN, self).__init__()	는 Fashin_DNN 라는 부모(super) 클래스 
	

	# nn 은 딥러닝 모델구성에 필요한 모듈이 모듈이 모여있는 패키지 
	# Linear 은 단순 선형 회귀 모델
	
	# nn.Linear(in_features=784, out_features=256) 파라미터
	# in_features : 입력의 크기
	# out_feautes : 출력의 크기
	# 데이터 연산이 진행되는 forward() 부분에는 첫 번째 파라미터 값(in_features)만 넘겨주게 되며,
	# 두 번째 파라미터(out_features) 에서 정의된 크기가 forward() 연산의결과


	# torch.nn.Dropout(p) 는 입력을 확률 P로 무작위 0으로 만드는 레이어
	# 이것은 일종의 regularization 기법으로 모델이 training 데이터에 overfitting 되는것을 방지
	# nn.Dropout(0.25) 는 입력이 25%를 0으로 만든다는 의미

	# forward() 함수는 모델에 학습데이터를 입력받아서 순전파 연산을 진행하는 함수이며, 객체를 데이터와 함께 호출하면 자동으로 실행
	# .view(-1,784)는 2차원 텐서로 변경하되, (? ,784)의 크기로 볍ㄴ경하라는 의미
	# 첫번째 차원 -1은 사용자가 잘모르겠으니 파이토치에 맡기겠으며, 두번째 차원의 길이는 784를 가지도록 하라는 의미
	# .reshape 함수와 같은 역할
	


	# 7. 심층 신경망에서 필요한 파라미터 정의

learning_rate = 0.001
model = Fashin_DNN().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

# 모델을 학습시키기 전에 손실함수,학습률,옵티마이저에 대해 정희
# 옵티마이저를 위한 경사하강법은 Adam 을사용하며, 학습률을 의미하는 lr은 0.001을 사용한다는 의미


# 8. 심층 신경망을 이용한 모델학습

num_epochs = 20
count = 0

loss_list = []
iteration_list = []
accuracy_list = []

predictions_list = []
labels_list = []

for epoch in range(num_epochs):
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        # 모델에 학습 데이터 입력
        train = images.view(100, 1, 28, 28)
        labels = labels

        outputs = model(train)  # 예측값 계산
        loss = criterion(outputs, labels)  # 손실 계산

        # 그래디언트 값 초기화 및 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        count += 1

        # 테스트 정확도 계산
        if (count % 50) == 0:
            total = 0
            correct = 0
            for images, labels in test_loader:
                images, labels = images.to(device), labels.to(device)

                test = images.view(-1, 1, 28, 28)
                outputs = model(test)
                predictions = torch.argmax(outputs, 1).to(device)

                correct += (predictions == labels).sum()
                total += len(labels)

            accuracy = 100. * correct / total  # 정확도 계산
            loss_list.append(loss.item())  # 손실 값을 item()으로 저장
            iteration_list.append(count)
            accuracy_list.append(accuracy)

            # 정확도 및 손실 출력
            print(f'Iteration: {count}, Loss: {loss.item()}, Accuracy: {accuracy:.2f}%')
            
# 학습 완료 후 시각화
plt.figure(figsize=(12, 5))

# 손실 그래프
plt.subplot(1, 2, 1)
plt.plot(iteration_list, loss_list, label='Loss', color='red')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.legend()

# 정확도 그래프
plt.subplot(1, 2, 2)
plt.plot(iteration_list, accuracy_list, label='Accuracy', color='blue')
plt.xlabel('Iterations')
plt.ylabel('Accuracy (%)')
plt.title('Training Accuracy')
plt.legend()

plt.tight_layout()  # 레이아웃 조정
plt.show()                 