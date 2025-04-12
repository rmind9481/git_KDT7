import spacy

# 한국어 모델 로드
KO_MODEL = "ko_core_news_sm"

# 한국어 분석기 생성
nlp = spacy.load(KO_MODEL)


print(type(nlp))