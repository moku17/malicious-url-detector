import streamlit as st
import joblib

# 모델 & 벡터 불러오기
model = joblib.load("url_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("🔍 웹 기반 악성 URL 판별기")
st.write("아래에 URL을 입력하면 악성 여부를 예측합니다.")

# 입력창
user_input = st.text_input("URL 입력")

# 검사 버튼
if st.button("검사하기"):
    if user_input:
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]
        if prediction == 1:
            st.error("🚨 악성 URL입니다!")
        else:
            st.success("✅ 정상 URL입니다.")
    else:
        st.warning("URL을 입력해주세요.")