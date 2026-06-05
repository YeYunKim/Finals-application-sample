import streamlit as st

st.set_page_config(page_title="분수 퀴즈", page_icon="🧠")

st.title("🧠 분수 퀴즈")
st.write("전체를 똑같이 5로 나눈 것 중 3조각을 나타내는 분수를 골라 보세요!")

options = ["1/5", "3/5", "5/3", "2/5"]
choice = st.radio("문제: 전체를 똑같이 5로 나눈 것 중 3조각을 나타내는 분수는 무엇일까요?", options)

if st.button("정답 제출하기"):
    if choice == "3/5":
        st.balloons()
        st.success("정답입니다! 🎉 분수 마스터가 되었군요!")
    else:
        st.error("다시 한 번 생각해보세요! 할 수 있어요!")
