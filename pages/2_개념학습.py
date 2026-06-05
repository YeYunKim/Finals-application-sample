import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="분수 개념 학습", page_icon="🍕")

st.title("🍕 분수 피자로 분수 알아보기")
st.write("슬라이더를 움직여서 피자 조각을 똑같이 나누어 보고, 분수의 의미를 직접 확인해 보세요.")

st.sidebar.header("분수 만들기")
denominator = st.sidebar.slider("분모 (전체 조각 수)", min_value=1, max_value=8, value=4)
numerator = st.sidebar.slider("분자 (선택한 조각 수)", min_value=1, max_value=denominator, value=1)

sizes = [numerator, denominator - numerator]
colors = ["#FFD700"] * numerator + ["#E5E5E5"] * (denominator - numerator)

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(
    sizes,
    colors=colors,
    startangle=90,
    wedgeprops={"linewidth": 2, "edgecolor": "white"},
)
ax.set_aspect("equal")
ax.set_title("피자 조각의 분수")
st.pyplot(fig)

st.write(
    f"전체를 똑같이 {denominator}개로 나눈 것 중 {numerator}개는 "
    f"{numerator}/{denominator} 입니다."
)

if numerator == 1 and denominator > 1:
    st.success("선생님의 팁: 1/{}는 단위분수예요! 한 조각을 나타내는 가장 기본적인 분수랍니다.".format(denominator))
elif numerator < denominator:
    st.info("선생님의 팁: {} / {}는 진분수예요. 전체보다 작은 양을 나타냅니다.".format(numerator, denominator))
else:
    st.warning("선생님의 팁: {} / {}는 가분수예요. 전체를 다 먹은 경우와 같은 뜻이니 조심해요!".format(numerator, denominator))
