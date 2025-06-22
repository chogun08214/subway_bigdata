import streamlit as st

st.markdown("<h1>서울시 지하철 호선별 역별 시간대별 승하차 인원 정보</h1>", unsafe_allow_html=True)


image_url1 = "https://www.sisul.or.kr/open_content/skydome/images/img_subway.png" 
image_url2 = "https://velog.velcdn.com/images/ljs7463/post/744d448c-ba31-4263-8c6b-b4001d1e1a84/image.png"

col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3>서울시 지하철 노선도</h3>", unsafe_allow_html=True)
    st.markdown(f"<img src='{image_url1}' width='800' height='800'>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3>서울시 구글맵</h3>", unsafe_allow_html=True)
    st.markdown(f"<img src='{image_url2}' width='800' height='800'>", unsafe_allow_html=True)


