# 1. 데이터 수집
# 2. 텍스트 정제 / 전처리 (정규화 + 토큰화 + 불용어 제거 등)
# 3. 탐색적 데이터 분석 (EDA)
# 4. 단어 사전 구축 / 벡터화
# 5. 임베딩 or 벡터화 (Embedding / TF-IDF / Word2Vec / BERT etc.)
# 6. 모델 학습 (전통 ML or 딥러닝)
# 7. 모델 튜닝 (하이퍼파라미터 / 교차 검증 등)
# 8. 성능 평가 (정확도 외에도 F1, Recall, Confusion Matrix 등)
# 9. 예측 결과 해석 / 시각화
# 10. 서빙 / 배포 (옵션)
import pandas as pd

# 네이버 감정 데이터셋

train = pd.read_csv(r'C:\Users\rmind\Desktop\git_KDT7\00.Study\NLP\LLM_Data\ratings_train.txt', sep='\t')
test = pd.read_csv(r'C:\Users\rmind\Desktop\git_KDT7\00.Study\NLP\LLM_Data\ratings_test.txt', sep='\t')



# ============================================================================================================
# 텍스트 정제 / 전처리
# ============================================================================================================

import re
from konlpy.tag import Okt

okt = Okt()

def clean_text(text):
    text = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", str(text))
    return text

def tokenize(text):
    return okt.morphs(clean_text(text), stem=True)

train['tokens'] = train['document'].apply(tokenize)



# ============================================================================================================
#  EDA (탐색적 데이터 분석)
# ============================================================================================================
import matplotlib.pyplot as plt
from collections import Counter

lengths = train['tokens'].apply(len)
plt.hist(lengths, bins=50)
plt.title("Token Length Distribution")
plt.show()

word_counts = Counter([token for tokens in train['tokens'] for token in tokens])
print(word_counts.most_common(10))

# ============================================================================================================
# 단어 사전 구축
# ============================================================================================================
vocab_size = 10000
vocab = {word: idx+2 for idx, (word, _) in enumerate(word_counts.most_common(vocab_size))}
vocab["<PAD>"] = 0
vocab["<UNK>"] = 1


# ============================================================================================================
# 임베딩 or 벡터화
# ============================================================================================================

def encode(tokens):
    return [vocab.get(token, 1) for token in tokens]

def pad(seq, max_len=100):
    return seq[:max_len] + [0] * (max_len - len(seq))

train['input_ids'] = train['tokens'].apply(lambda x: pad(encode(x)))

import torch
X_train = torch.tensor(train['input_ids'].tolist())
y_train = torch.tensor(train['label'].tolist())


# ============================================================================================================
# 모델학습 LSTM 모델
# ============================================================================================================
import torch.nn as nn

class SentimentModel(nn.Module):
    def __init__(self, vocab_size, embed_dim=100, hidden_dim=64):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.embedding(x)
        _, (hidden, _) = self.lstm(x)
        out = self.fc(hidden[-1])
        return self.sigmoid(out).squeeze()
    
# ============================================================================================================
#  모델 튜닝
# ============================================================================================================

model = SentimentModel(len(vocab)).to('cpu')  # 'cuda' 가능
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

from torch.utils.data import DataLoader, TensorDataset
loader = DataLoader(TensorDataset(X_train, y_train), batch_size=64, shuffle=True)

for epoch in range(3):
    total_loss = 0
    model.train()
    for x_batch, y_batch in loader:
        optimizer.zero_grad()
        preds = model(x_batch.float())
        loss = criterion(preds, y_batch.float())
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1} Loss: {total_loss:.4f}")


# ============================================================================================================
#  성능 평가        정확도 / 정밀도 / 재현율
# ============================================================================================================


from sklearn.metrics import accuracy_score, precision_score, recall_score

model.eval()
with torch.no_grad():
    preds = model(X_train).numpy()
    y_pred = (preds > 0.5).astype(int)

acc = accuracy_score(y_train, y_pred)
prec = precision_score(y_train, y_pred)
rec = recall_score(y_train, y_pred)

print(f"Accuracy: {acc:.4f}, Precision: {prec:.4f}, Recall: {rec:.4f}")


# ============================================================================================================
#  예측 결과 해석 / 시각화      가장 부정적인 문장 살펴보기
# ============================================================================================================

train['score'] = preds
worst = train.sort_values(by='score').head(5)
print(worst[['document', 'score']])


# ============================================================================================================
#   서빙 (옵션) 예제: 간단한 예측 함수 만들기
# ============================================================================================================
def predict(text):
    tokens = tokenize(text)
    ids = torch.tensor(pad(encode(tokens))).unsqueeze(0)
    pred = model(ids.float()).item()
    return "긍정" if pred > 0.5 else "부정"

print(predict("이 영화 너무 감동적이에요"))