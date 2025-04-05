# 모듈 로딩
# Dataset => 클래스 => 데이터셋 관리
# Model 클래스 => 딥러닝 모델 구조
# Trainer 클래스 => 학습/평가 루프 관리
# 실행


# Dataset 클래스

import torch
from torchvision import datasets,transforms
from torch.utils.data import DataLoader, Dataset
import pandas as pd

class MNISTData:
	def __init__(self, batch_size=64):
		# 데이터 전처리 : 이미지를 Tensor로 변환하고 0~1로 정규화
		transform = transforms.Compose([transforms.ToTensor(),
								  transforms.Normalize((0.5,),(0.5,)) 	# 평균, 표준편차 정규화
								  ])
		
		self.train_data = datasets.MNIST(root='../../Data', train=True, download=True, transform=transform)
		self.test_data = datasets.MNIST(root='../../Data', train=False, download=True, transform=transform)
		
		# DataLoadr 생성
		self.train_loader = DataLoader(self.train_data, batch_size=batch_size, shuffle=True)
		self.test_loader = DataLoader(self.test_data, batch_size=batch_size, shuffle=False)

# Model 클래스

import torch.nn as nn
import torch.nn.functional as F

class MINISTModel(nn.Module):
	def __init__(self):
		super(MINISTModel,self).__init__()
		# 입력층 => 은닉층
		self.fc1 = nn.Linear(28*28,128)
		self.fc2 = nn.Linear(128,64)
		self.fc3 = nn.Linear(64,10)

	def forward(self, x ):
		# 2D 이미지 => 1D 벡터
		x = x.view(-1,28*28)
		x = F.relu(self.fc1(x))
		x = F.relu(self.fc2(x))
		# CrossEntropyLoss 가  softmax 포함
		x = self.fc3(x)

		return x
	

# Trainer 클래스

import torch.optim as optim

class Trainer:
	def __init__(self, model, train_loader, test_loader):
		self.model = model
		self.train_loader = train_loader
		self.test_loader = test_loader
		# 다중분류용 손실 함수
		self.criterion = nn.CrossEntropyLoss()
		self.optimizer = optim.Adam(model.parameters(), lr=0.0001)
		
	def train(self, epochs =5 ):
		self.model.train()
		for epoch in range(epochs):
			runing_loss = 0 
			for inputs, labels in self.train_loader:
				# 순전파
				outputs = self.model(inputs)
				loss = self.criterion(outputs, labels)
				
				# 역전파 + 업데이트 
				self.optimizer.zero_grad()
				loss.backward()
				self.optimizer.step()

				runing_loss += loss.item()
			print(f'{epoch+1}, loss : {runing_loss/len(self.train_loader):.4f}')

	def evaluate(self):
		self.model.eval()
		correct = 0 
		total = 0

		with torch.no_grad():
			for inputs, labels in self.test_loader:
				outputs = self.model(inputs)
				_, predicated = torch.max(outputs,1)
				total += labels.size(0)
				correct += (predicated == labels).sum().item()
		
		print(f'테스트 정확도: {100* correct/ total:.2f}%')

# 실행

# 데이터 준비
data = MNISTData(batch_size=64)

# 모델 생성
model = MINISTModel()

# Trainer 생성
trainer = Trainer(model, data.train_loader, data.test_loader)

# 학습
trainer.train(epochs=5)

# 평가
trainer.evaluate()