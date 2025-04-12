# 1. 데이터 로딩
# 2. 텍스트 전처리
# 3. 단어 사전 구축
# 4. 단어 토큰화
# 5. 임베딩
# 6. 모델학슴 (LSTM)
# 7. 성능평가

import pandas as pd

# 네이버 감정 데이터셋

train_df = pd.read_csv(r'C:\Users\rmind\Desktop\git_KDT7\00.Study\NLP\LLM_Data\ratings_train.txt', sep='\t')
test_df = pd.read_csv(r'C:\Users\rmind\Desktop\git_KDT7\00.Study\NLP\LLM_Data\ratings_test.txt', sep='\t')

train_df = train_df.dropna()
test_df = test_df.dropna()
# print(train_data)

# ============================================================================================================
# 텍스트 전처리
# ============================================================================================================
from konlpy.tag import Okt
import re

okt = Okt()

def clean_and_tokenize(text):
    text = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", text)
    return okt.morphs(text, stem=True)

train_df['tokens'] = train_df['document'].apply(clean_and_tokenize)
test_df['tokens'] = test_df['document'].apply(clean_and_tokenize)

from collections import Counter

counter = Counter()
for tokens in train_df['tokens']:
    counter.update(tokens)

vocab_size = 10000
vocab = {word: idx + 2 for idx, (word, _) in enumerate(counter.most_common(vocab_size))}
vocab["<PAD>"] = 0
vocab["<UNK>"] = 1


def encode(tokens):
    return [vocab.get(token, 1) for token in tokens]

train_df['input_ids'] = train_df['tokens'].apply(encode)
test_df['input_ids'] = test_df['tokens'].apply(encode)

from torch.nn.utils.rnn import pad_sequence
import torch

MAX_LEN = 100

def pad_tensor(seq, max_len=MAX_LEN):
    seq = torch.tensor(seq[:max_len])
    return torch.cat([seq, torch.zeros(max_len - len(seq), dtype=torch.long)])

X_train = torch.stack([pad_tensor(x) for x in train_df['input_ids']])
y_train = torch.tensor(train_df['label'].values)


from torch.utils.data import TensorDataset, DataLoader

train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64)






import torch.nn as nn

class SentimentModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        embedded = self.embedding(x)
        _, (hidden, _) = self.lstm(embedded)
        out = self.fc(hidden[-1])
        return self.sigmoid(out).squeeze()
    



model = SentimentModel(vocab_size=len(vocab), embed_dim=100, hidden_dim=64)
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

for epoch in range(3):
    model.train()
    total_loss = 0
    for x_batch, y_batch in train_loader:
        x_batch, y_batch = x_batch.to(device), y_batch.float().to(device)
        optimizer.zero_grad()
        y_pred = model(x_batch)
        loss = criterion(y_pred, y_batch)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1} Loss: {total_loss:.4f}")





model.eval()
correct, total = 0, 0
with torch.no_grad():
    for x_batch, y_batch in test_loader:
        x_batch, y_batch = x_batch.to(device), y_batch.to(device)
        y_pred = model(x_batch)
        preds = (y_pred > 0.5).int()
        correct += (preds == y_batch).sum().item()
        total += y_batch.size(0)
print(f"Test Accuracy: {correct / total:.4f}")