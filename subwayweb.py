import streamlit as st

st.set_page_config(
    page_title="서울시 지하철 승하차 인원 정보",
    layout="wide"
    )

pages = {
    "  ":[
        st.Page("홈페이지.py", title="홈페이지")
    ],

    "승하차 인원 정보": [
        st.Page("승차 인원 정보.py", title="승차 인원 정보"),
        st.Page("하차 인원 정보.py", title="하차 인원 정보"),
    ],
    "역별 인원 정보": [
        st.Page("역별 하루 평균 승차.py", title="역별 하루 평균 승차"),
        st.Page("역별 하루 평균 하차.py", title="역별 하루 평균 하차"),
    ],
    "역": [
        st.Page("line1.py", title="1호선")
    ]
}

pg = st.navigation(pages)
pg.run()