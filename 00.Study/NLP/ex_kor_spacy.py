# 자연어 한구어 형태소 모델

# 모듈로딩

import spacy
from konlpy.corpus import *
import string


# 데이터 및 모델 로딩

LAW_FILE = kolaw.fileids()[0]

### 한국어 모델 설정
KO_MODEL = 'ko_core_news_sm'

### 구두점 및 불필요 기호
PUNC    = string.punctuation + "★"

## 데이터 로딩 => 줄 단위로 읽어오기 
LAW_CORPUS = kolaw.open(LAW_FILE).readlines()

## 형태소 모델 로딩
MORPH_MODEL = spacy.load(KO_MODEL)

print(f'[정리 전] {len(LAW_CORPUS)}개')
NUMS = len(LAW_CORPUS)

for idx in range(NUMS-1, 0, -1):
    LAW_CORPUS[idx] = LAW_CORPUS[idx].strip()
    LAW_CORPUS[idx] = LAW_CORPUS[idx].replace('\n','')

    if not len(LAW_CORPUS[idx]): del LAW_CORPUS[idx]

print(f'[정리 후] {len(LAW_CORPUS)}개')


# Doc 타입은 token 으로 구성 => token 객체.속성명

#print(LAW_CORPUS)

# 형태소 분석 적용
print("\n[형태소 분석]")

save_tokens=[]

for line in LAW_CORPUS:
    doc = MORPH_MODEL(line)
    #print(f"\n원문: {line}")
    print("형태소 및 품사:")
    for token in doc:
        if not (token.is_stop or token.is_punct) :  
            save_tokens.append(token)
        print(f"{token.text} ({token.pos_})", end=' ')
    print()