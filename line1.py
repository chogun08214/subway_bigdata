import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 로딩
@st.cache_data
def load_data():
    return pd.read_csv("서울시 지하철 호선별 역별 시간대별 승하차 인원 정보_202501까지.csv")

df = load_data()

# 지하철 역 목록 (1호선만 예시)
line1_stations = {
    1: "소요산",    2: "동두천",    3: "보산",    4: "동두천중앙",    5: "지행",
    6: "덕정",    7: "덕계",    8: "양주",    9: "녹양",    10: "가능",
    11: "의정부",    12: "회룡",    13: "망월사",    14: "도봉",    15: "도봉산",
    16: "방학",    17: "창동",    18: "녹천",    19: "월계",    20: "광운대",
    21: "석계",    22: "신이문",    23: "외대앞",    24: "회기",    25: "청량리",
    26: "제기동",    27: "신설동",    28: "동묘앞",    29: "동대문",    30: "종로5가",
    31: "종로3가",    32: "종각",    33: "시청",    34: "서울역",    35: "남영",
    36: "용산",    37: "노량진",    38: "대방",    39: "신길",    40: "영등포",
    41: "신도림",   42: "구로",    43: "구일",    44: "개봉",    45: "오류동",
    46: "온수",    47: "역곡",    48: "소사",    49: "부천",    50: "중동",
    51: "송내",    52: "부개",    53: "부평",    54: "백운",    55: "동암",
    56: "간석",   57: "주안",    58: "도화",    59: "제물포",    60: "도원",
    61: "동인천",    62: "인천",    63: "가산디지털단지",    64: "독산",    65: "금천구청",
    66: "광명",    67: "석수",    68: "관악",    69: "안양",    70: "명학",
    71: "금정",   72: "군포",    73: "당정",    74: "의왕",    75: "성균관대",
    76: "화서",    77: "수원",    78: "세류",    79: "병점",    80: "세마",
    81: "오산대",    82: "오산",    83: "진위",    84: "송탄",    85: "서정리",
    86: "지제",    87: "평택",    88: "성환",    89: "직산",    90: "두정",
    91: "천안"
}

st.markdown("<h2 style='text-align: center;'>서울시 지하철 시간대별 승차 인원</h2>", unsafe_allow_html=True)

station_items = list(line1_stations.items())
num_cols = 6
for i in range(0, len(station_items), num_cols):
    cols = st.columns(num_cols)
    for j, (station_id, station_name) in enumerate(station_items[i:i + num_cols]):
        with cols[j]:
            if st.button(station_name, key=f"station_{station_id}"):
                # 선택된 역의 데이터 필터링
                filtered = df[(df["사용월"] == 202505) & (df["지하철역"] == station_name)]

                if not filtered.empty:
                    time_cols = [col for col in df.columns if '승차인원' in col and '하차' not in col]
                    time_data = filtered[time_cols].iloc[0]

                    # 그래프 출력
                    fig, ax = plt.subplots(figsize=(12, 6))
                    time_data.plot(kind='bar', ax=ax)
                    ax.set_title(f"{station_name}역 시간대별 승차 인원 (2025년 5월)", fontsize=16)
                    ax.set_xlabel("시간대", fontsize=12)
                    ax.set_ylabel("승차 인원", fontsize=12)
                    ax.tick_params(axis='x', rotation=45)
                    st.pyplot(fig)
                else:
                    st.warning(f"{station_name}역의 데이터가 없습니다.")
