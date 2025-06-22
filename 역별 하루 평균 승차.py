import streamlit as st
import pathlib

st.markdown("<h1>역별 하루 평균 승차차</h1>", unsafe_allow_html=True)

html_path = pathlib.Path("C:/Users/tkfka/opensource/202501-05_역별_하루평균승차_heatmap_corrected.html")
html_content = html_path.read_text(encoding='utf-8')

st.components.v1.html(html_content, height = 800, width = 1000)