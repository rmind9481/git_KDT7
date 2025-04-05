import pandas as pd 
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

class PenguinData(Dataset):
	
	def __init__(self,X,y):
		super().__init__()
		self.X = torch.tensor(X, dtype=torch.float32)
		self.y = torch.tensor(y, dtype=torch.long)

	def __len__(self):
		return len(self.X)
	
	def __getitem__(self, index):
		return self.X[index], self.y[index]
	
class DataHandler :
	def __init__(self,batch_size = 32):
		df = pd.read_csv('../../Data/penguins.csv')
		df = df.dropna()
		print(df.info(), df.describe())
		print(f'coulums : {df.columns}')
		# 특성 , 타겟 분리
		# 
		# species, island, sex
		#
		X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].values
		y = LabelEncoder().fit_transform(df['species'])

		# 데이터 전처리
		scaler = StandardScaler()
		X = scaler.fit_transform(X)
		
		X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

		# Dataset, DataLoader 생성
		self.train_dataset = PenguinData(X_train, y_train)
		self.test_dataset = PenguinData(X_test, y_test)

		self.train_loader =DataLoader(self.train_dataset, batch_size=batch_size, shuffle=True)
		self.test_loader =DataLoader(self.test_dataset, batch_size=batch_size, shuffle=False)

# Dynamic 모델클래스

import torch.nn as nn
import torch.nn.functional as F

class Dynamic_Model(nn.Module):
	def __init__(self, input_dim, hidden_dims, output_dim):
		super(Dynamic_Model, self).__init__()
		
		layers = []
		last_dim = input_dim
		
		# 은닉층 추가
		for h_dim in hidden_dims:
			layers.append(nn.Linear(last_dim, h_dim))
			layers.append(nn.ReLU())
			last_dim = h_dim

		# 출력층
		layers.append(nn.Linear(last_dim,output_dim))
		self.network = nn.Sequential(*layers)

	def forward(self, x):
		return self.network(x)
	

	# Trainer 클래스
	
import torch.optim as optim

class Trainer:
	def __init__(self, model, train_loader, test_loader):
		self.model = model
		self.train_loader = train_loader
		self.test_loader = test_loader
		self.criterion = nn.CrossEntropyLoss()
		self.optimizer = optim.Adam(model.parameters(), lr=0.001)

	def train(self, epochs=50):
		self.model.train()
		for epoch in range(epochs):
			running_loss = 0.0
			for inputs, labels in self.train_loader:
				outputs = self.model(inputs)
				loss = self.criterion(outputs, labels)

				self.optimizer.zero_grad()
				loss.backward()
				self.optimizer.step()

				running_loss += loss.item()
			avg_loss = running_loss/ len(self.train_loader)
			print(f'Epoch {epoch+1}, Loss: {avg_loss:.4f}')

	def evaluate(self):
		self.model.eval()
		correct = 0
		total = 0

		with torch.no_grad():
			for inputs, labels in self.test_loader:
				outputs = self.model(inputs)
				_, predicted = torch.max(outputs, 1)
				total += labels.size(0)
				correct += (predicted == labels).sum().item()
		
		print(f'테스트 정확도: {100* correct / total:.2f}%')

data = DataHandler(batch_size=16)

model = Dynamic_Model(input_dim=4, hidden_dims=[64,32], output_dim=3)

# Trainer  생성

trainer = Trainer(model, data.train_loader, data.test_loader)

# 학습 
trainer.train(epochs=30)

# 평가
trainer.evaluate()

