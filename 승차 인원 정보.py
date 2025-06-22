import streamlit as st
import pathlib

st.markdown("<h1>시간별 승차 인원 변화</h1>", unsafe_allow_html=True)

html_path = pathlib.Path("C:/Users/tkfka/opensource/animated_heatmap_승차_202505.html")
html_content = html_path.read_text(encoding='utf-8')

st.components.v1.html(html_content, height=800, width = 1000)


