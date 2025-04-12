import torch
import torch.nn as  nn
import torch.nn.functional as F


import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets,transforms

# 데이터 로딩 및 전처리

transform = transforms.Compose([
	# 텐서로 변환
	# ToTenser() => 이미지를 Pytorch 텐서로 변환
	# 0~255 이미지를 [0,1] 범위로 정규화
	transforms.ToTensor(),
	# 데이터 졍규화
	# Normalize  : 이미지를 정규화 하여 평균이 0, 표준편차가 1에 가까운 분포를 만듬 
	transforms.Normalize((0.5,),(0.5,)) 
])

FILE_PATH = '../../Data'

# MNIST 데이터셋 다운로드
train_dataset = datasets.MNIST(root=FILE_PATH, train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root=FILE_PATH, train=False, download=True, transform=transform)
print(f'train dataset :\n{train_dataset},test_dataset : \n{test_dataset}')
print(f'train type :\n{type(train_dataset)},test type : \n{type(test_dataset)}')


# DataLoader 로 배치 단위로 데이터 로딩

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

print(f'train loader :\n{train_loader},test_loader : \n{test_loader}')
print(f'train type :\n{type(train_loader)},test type : \n{type(test_loader)}')
#==================================================================================================
#  CNN 모델구성
#==================================================================================================
#	
#
#
#
#==================================================================================================

class CNN(nn.Module):

#==================================================================================================
	# 모델 초기화  nn.Module 을 상속받아서 CNN 클래스를 정의
	def __init__(self):
		super().__init__()
		
		# Convolutional Layer 1
		# Conv2d : 2D Convolution Layer 를 정의한다.
		# 첫번째 Conv2d는 1채널 입력을 32채널 출력으로 변환
		self.conv1 = nn.Conv2d(1,32,kernel_size=3, padding=1)
		
		# nn.Conv2d(in_channels, out_channels, kernel_size, padding)
		# in_channels (출력 채널수) : 
		# 입력 이미지의 채널 수를 의미한다.
		# 손글씨의 이미지는 흑백이므로 채널수는 1 
		
		# out_channels (출력 채널수): 이 레이어에서 생성할 필터(또는 커널)의 개수
		# 이경우 32개의 필터를 사용하여 출력 채널수를 32로 설정
		# Kernel_size : 커널(필터)의 크기 3x3 크기의 커널을 사용
		# padding : 이미지의 경계를 처리할 때 사용하는 값
		# Padding = 1 로 설정하여 이미지 크기를 유지하도록한다.


		# MaxPool2d : MaxPooling 을 사용하여 이미지 크기를 축소
		self.pool = nn.MaxPool2d(kernel_size=2,stride=2)
		
		# nn.MaxPool2d(kernel_size, stride)
		# kernel_size : 풀링 연산에 사용할 커널의 크기 2x2 크기의 풀링 커널을 사용
		# stride : 커널을 이동시키는 간격, 2로 설정하여 풀링 연산을 한번에 2칸씩 이동

		# MaxPool2d 는 이미지를 축소하는 역할을한다.
		# 2x2 크기의 풀링 커널을 사용하여 이미지의 크기를 절반으로 줄인다.

		# Convolutional Layer 2
		# 두번째 Conv2d는 32체널을 64체널로 변환
		self.conv2 = nn.Conv2d(32,64,kernel_size=3,padding=1)
		# 첫번째 conv1 레이어의 출력인 32채널 이미지를 입력으로 받는다.
		# 출력 채널수 64로 설정하여 32채널을 64채널로 변환

	

		# Fully Connected Layer (Dense Layer)

		# 64개의 필터 , 7x7 크기 (이미지 크기 축소후)
		# Linear : Fully Connected Layer 를 정의한다. 
		# 마지막 Linear는 10개의 클래스로 분류
		self.fc1 = nn.Linear(64*7*7,128) 

		# fc1: Fully Connected Layer (완전 연결층)
		# nn.Linear(in_features, out_features) 는 
		# 입력 특성수 (in_features)와 
		# 출력 특성수(out_features) 를 지정하는 레이어
		# 첫번째 Fully Connected Layer의 
		# 입력크기 : 64*7*7 
		# 64개의 필터와 7x7 크기의 이미지가 Flatten(1D 벡터로 변환)
		# => 64*7*7 크기의 벡터로 연결된다
		# 출력 크기는 128 으로 설정되어, 이레이어에서는 128개의 뉴런을 가진다.

		# 10개의 클래스로 분류
		self.fc2 = nn.Linear(128,10) 
		# fc2: 마지막 Fully Connected Layer
		# 이 레이어는 128개의 입력 뉴런을 받아서 10개의 출력 뉴런을 생성
		# 출력은 10개의 클래스로 분류하기 위한 확률값

#==================================================================================================
	# 순전파
	# 모델의 계층 순서
	# X <= 모델에 입력으로 들어오는 데이터,
	
	# MNIST 같은경오 (batch_size, 1,28,28) 형태의 텐서가 들어온다.

	def forward(self, x):
		# Convolution + ReLu + Maxpooling
		# 첫번째 Convolution Layer
		x = self.pool(torch.relu(self.conv1(x)))
		# self.conv1(x) 입력 x 에 첫번째 Convolution Layer 인  conv1 을 적용
		# 32 채널의 특성 맵을 생성
		# torch.relu() : ReLU 활성화 함수를 적용하여 음수 값을 0으로 바꾸고, 양수는 그대로 유지하여 빈선형성을 추가
		# self.pool() : MaxPool2d 를 적용하여 특성 맵의 크기를 절반으로 축소
		

		# 두번째 Convloution Layer
		x = self.pool(torch.relu(self.conv2(x)))
		
		# Flatten
		x = x.view(-1,64*7*7)

		# Fully Connected layer
		# 
		x = torch.relu(self.fc1(x))
		x = self.fc2(x) # 최종출력
		return x
	
# 입력 이미지 (28x28 크기, 1채널)

# Convolution Layer 1: 32개의 필터로 이미지 특징 추출
# MaxPooling: 이미지 크기 절반 축소

# Convolution Layer 2: 64개의 필터로 더 복잡한 특징 추출
# MaxPooling: 이미지 크기 절반 축소
# Flatten: 2D 텐서를 1D 벡터로 변환

# Fully Connected Layer 1: 128개의 뉴런을 사용하여 특징을 더 추상화
# Fully Connected Layer 2 (출력층): 10개의 뉴런으로 분류 결과 출력


#==================================================================================================
#==================================================================================================


# 모델 초기화

model = CNN()

# 손실함수 함수 및 최적화 방법 설정
# 다중 클래스 분류 문제 손실 함수
criterion = nn.CrossEntropyLoss()

# Adam 옵티마이져 를 사용하여 모델 파라미터를 업데이트
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 훈련
epochs = 5
for epoch in range(epochs):
	# 훈련모드
	model.train()
	running_loss =0.0
	correct = 0
	total = 0

		# 예측값, 정답
	for input, labels in train_loader:
		# 기울기 초기화
		optimizer.zero_grad()

		outputs = model(input)
		# 손실계산
		loss = criterion(outputs,labels)
		# 역전파
		loss.backward()
		# 파라미터 업데이트
		optimizer.step()

		running_loss += loss.item()
		# 예측된 레이블
		_, predicted = torch.max(outputs,1)

		total += labels.size(0)
		# 정확도 계산
		correct +=(predicted == labels).sum().item()

	print(f"Epoch {epoch+1}/{epochs}, Loss: {(running_loss/len(train_loader)):.4f}, Accuracy: {(100 * correct / total):.4f}%")

# =======================================================================================
# 모델 평가
# =======================================================================================

# 평가모드
model.eval()
correct = 0
total = 0

# 평가 중에는 기울기 계산을 하지않음
with torch.no_grad():
	for inputs, labels in test_loader:
		outputs = model(inputs)
		_, predicted = torch.max(outputs,1)
		total += labels.size(0)
		correct += (predicted == labels).sum().item()

print(f"Test Accuracy: {(100 * correct / total):.4f}%")