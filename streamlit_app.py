import streamlit as st

st.set_page_config(page_title="분수 도입 수업", page_icon="🍕")

st.title("🍕 피자처럼 분수를 알아봐요!")
st.write("친구 4명이 피자 1판을 똑같이 나누면, 한 사람은 몇 조각씩 먹을까요?")
st.write("이 문제를 먼저 생각해 보고, 다음 페이지에서 분수 피자로 직접 확인해 봐요.")

icebreaker = st.radio(
    "문제: 피자 1판을 4명이 똑같이 나누면 한 사람당 몇 조각일까요?",
    ["1/4 조각", "2/4 조각", "3/4 조각", "4/4 조각"],
    index=0,
)

if st.button("정답 확인하기"):
    if icebreaker == "1/4 조각":
        st.success("정답이에요! 피자 1판을 4명이 똑같이 나누면 한 사람당 1/4 조각씩 먹어요.")
    else:
        st.info("아직 조금 더 생각해볼까요? 4명이 똑같이 나누면 한 사람당 1/4 조각이에요.")

    st.caption("이제 분수 피자 페이지에서 직접 조각을 확인해 보세요.")
    st.page_link("pages/2_개념학습.py", label="분수 피자 개념 학습으로 가기")
