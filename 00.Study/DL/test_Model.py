import torch                             # 토치
import torch.nn as nn                    # 인공신경망 관련 모듈
import torch.nn.functional as F          # 활성화, 손실 등 함수들 모듈
import torch.optim as optim              # 경사하강법 최적화 모듈
import pandas as pd
from torchvision import transforms
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from torch.utils.data import Dataset, DataLoader


train_Df = pd.read_csv('../Data/fashion-mnist_train.csv')
test_Df = pd.read_csv('../Data/fashion-mnist_test.csv')

plt.imshow(np.array(train_Df.iloc[2, 1:]).reshape(28, 28), cmap='gray')
plt.show()
# print(train_Df.info())
# print(train_Df.head())
# print(train_Df.nunique())
# print(train_Df.label.nunique())

print(f'train_Df.shape{train_Df.shape}')
print(f'test_Df.shape{test_Df.shape}')


# 최신버전 문법이므로 현재에서 안됨
# accelerator를 사용하려면 PyTorch 2.0 이상이 필요
# device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else 'cpu'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#print(torch.__version__)

print(f"Using {device} device")


# 모델 클래스 설계 =================================================================
# 회귀용 커스텀 모델
# 클래스 이름 : NeuralNetwork
# 부모 클레스 : nn.model
# feature => pixel1~784
# target => label   label 10
# 
# 모델층 구성  :		입력신호/			출력신호		활성화함수
#  - 입력측    :		784				   512				ReLu
#  - 은닉층    :		512				   512				ReLu
#  - 출력층	   : 		512					10				-	

class train_Dataset(Dataset):
    def __init__(self, data, transform=None):
        self.fasion_mnist = list(data.values)
        self.transform = transform
        label, img = [], []

        for one_line in self.fasion_mnist:
            label.append(one_line[0])
            img.append(one_line[1:])  # 이미지는 784개의 값

        self.label = np.array(label)
        # 이미지를 (28, 28, 1) 형태로 reshape
        self.img = np.array(img).reshape(-1, IMAGE_SIZE, IMAGE_SIZE, CHANNEL).astype('float32')

    def __len__(self):
        return len(self.label)

    def __getitem__(self, idx):
        label, img = self.label[idx], self.img[idx]
        if self.transform:
            img = self.transform(img)
        
        return label, img


class test_Dataset(Dataset):
    def __init__(self, data, transform=None):
        self.fashion_mnist = list(data.values)
        self.transform = transform
        img = []

        for one_line in self.fashion_mnist:
            img.append(one_line[1:])  # 이미지는 784개의 값

        # 이미지 크기 확인 후, 전체 데이터를 (28, 28, 1)로 reshape
        self.img = np.array(img).reshape(-1, IMAGE_SIZE, IMAGE_SIZE, CHANNEL).astype('float32')

    def __len__(self):
        return len(self.fashion_mnist)

    def __getitem__(self, idx):
        img = self.img[idx]
        if self.transform:
            img = self.transform(img)
        return img


BATCH_SIZE = 2500
LR = 5e-3
NUM_CLASS = 10
IMAGE_SIZE = 28
CHANNEL = 1
Train_epoch = 30

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

My_transform = transforms.Compose([
    transforms.ToTensor(), # default : range [0, 255] -> [0.0, 1.0]
])

Train_data = train_Dataset(train_Df, transform=My_transform)
Test_data = test_Dataset(test_Df, transform=My_transform)

Train_dataloader = DataLoader(dataset=Train_data,
                              batch_size=BATCH_SIZE,
                              shuffle=False)

Test_dataloader = DataLoader(dataset=Test_data,
                             batch_size=1,
                             shuffle=False)


class My_model(nn.Module):
    def __init__(self, num_of_class):
        super(My_model, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1),  # 28 * 28 * 16
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))  # 14 * 14 * 16
        
        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),  # 14 * 14 * 32
            nn.BatchNorm2d(32),
            nn.ReLU()
            # nn.MaxPool2d(kernel_size=2, stride=2)) 7 * 7 * 32
        )

        self.layer3 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )  # 7 * 7 * 64
        
        self.fc = nn.Linear(7 * 7 * 64, num_of_class)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        return out


# 1. 모델에 데이터 넣기  output = model(image)
# 2. 로스 구하기 loss = criterion(output, labe)
# 3. 옵티마이져 기울기 초기화 하기
# 4. 역적파 진행해주기
# 5. 최적화 과정진행

def train():
    model = My_model(NUM_CLASS).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)
    criterion = nn.CrossEntropyLoss()
    min_Loss = 100000
    for epoch in range(1, Train_epoch + 1):
        for batch_id, (label, image) in enumerate(Train_dataloader):
            label, image = label.to(device), image.to(device)
            output = model(image)
            loss = criterion(output, label)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if batch_id % 1000 == 0:
                print('Loss :{:.4f} Epoch[{}/{}]'.format(loss.item(), epoch, Train_epoch))
                if loss.item() < min_Loss:
                    torch.save(model, './best_model.pt')
                    min_Loss = loss.item()
                    print('Model save!! found minimum loss')
    return model

def test(model):
    model = torch.load('./best_model.pt')  # 모델 불러오기
    print('success load best_model')
    pred = []
    with torch.no_grad():
        correct = 0
        total = 0
        for image in Test_dataloader:
            image = image.to(device)

            outputs = model(image)

            predicted = np.array(torch.argmax(outputs, dim=1).cpu())
            pred.append(predicted)
    
    print(np.array(pred).flatten().shape)
    return np.array(pred).flatten()

if __name__ == '__main__':
    model = train()
    pred = test(model)

