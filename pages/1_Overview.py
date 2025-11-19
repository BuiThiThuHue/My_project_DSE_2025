import streamlit as st
import pandas as pd

from source_code import processing

# -----------------------------
# LOAD DATA WITH CACHE
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("d:/Study_Unimi/Coding_Python/Project_2025/My_project_DSE_2025/Dataset/songs_data.csv")

# -----------------------------
# INIT SESSION STATE
# -----------------------------
if "df" not in st.session_state:
    st.session_state["df"] = load_data()

df = st.session_state["df"]

# -----------------------------
# PAGE CONTENT
# -----------------------------
st.title("Tổng Quan Dữ Liệu")

st.subheader("Number of Songs per Year")
fig = processing.songs_per_year(df)  # Quan trọng
st.pyplot(fig)

# -----------------------------
# Stats
# -----------------------------
st.write("### Một vài thống kê nhanh:")
st.write(df.describe())

st.write("### 10 dòng đầu tiên của dữ liệu")
st.dataframe(df.head())

st.write("### Số lượng bài hát theo năm phát hành")
df = st.session_state["df"]
fig = processing.plot_top_artists(processing.top10_artist_songs(df))
st.pyplot(fig)
