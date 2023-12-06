import streamlit as st

# streamlit run ./app.py

st.set_page_config(
    page_title="뉴스 수집기",
    page_icon="./images/favicon.png"
)

st.title("NEWS COLLECTOR")
st.text("DAUM 뉴스를 수집합니다.")

with st.form(key="form"):
    category = st.text_input("뉴스 카테고리를 입력하세요.").strip()
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(category)