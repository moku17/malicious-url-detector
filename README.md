🛡️ 악성 URL 판별기 (Malicious URL Classifier)

이 프로젝트는 사용자가 입력한 URL이 정상(benign) 인지,  
또는 악성(phishing/malware/defacement) 인지를 분류하는  
머신러닝 기반 웹 애플리케이션입니다.


🔧 사용 기술

- Python (3.11+)
- Scikit-learn (Logistic Regression)
- Pandas
- TfidfVectorizer
- Streamlit (웹 UI)


📂 주요 파일

- `malicious_phish.csv` : 악성 URL 데이터셋
- `train_model.py` : 모델 학습 스크립트
- `app.py` : Streamlit 웹 앱
- `url_model.pkl` : 저장된 머신러닝 모델
- `vectorizer.pkl` : TF-IDF 벡터화 도구
