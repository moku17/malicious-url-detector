import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# 1. 데이터 불러오기
df = pd.read_csv("malicious_phish.csv")
print("✅ CSV 로드 완료")
print("전체 샘플 수:", len(df))
print("type 컬럼 값 종류:", df['type'].unique())
print("각 클래스 수:\n", df['type'].value_counts())

# 2. 라벨 처리 ('benign' = 0, 나머지 전부 = 1)
df['label'] = df['type'].apply(lambda x: 0 if x == 'benign' else 1)

# 3. 라벨 분포 확인
print("라벨 분포 (0: 정상, 1: 악성):\n", df['label'].value_counts())

# 4. 벡터화
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['url'])
y = df['label']

# 5. 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 6. 모델 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 7. 모델 저장
joblib.dump(model, "url_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ 모델 학습 및 저장 완료")