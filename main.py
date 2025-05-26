import streamlit as st
st.title('나의 첫 Streamlit 앱')
st.write('안녕하세요!')
import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 제목
st.title("🩺 당뇨병 진단 데이터 시각화")

# CSV 파일 불러오기
df = pd.read_csv("diabetes.csv")  # 직접 다운로드한 파일 경로

# 데이터 미리보기
st.subheader("데이터 미리보기")
st.dataframe(df)

# 유저 선택: X축, Y축
x_axis = st.selectbox("X축 열 선택", df.columns)
y_axis = st.selectbox("Y축 열 선택", df.columns, index=1)

# 그래프 그리기
st.subheader("📊 Plotly 시각화")
fig = px.scatter(df, x=x_axis, y=y_axis, color="Outcome",
                 title=f"{x_axis} vs {y_axis} (Outcome 별 색상)",
                 labels={"Outcome": "당뇨 여부 (0: 없음, 1: 있음)"})
st.plotly_chart(fig)
