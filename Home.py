import streamlit as st
import pandas as pd

# Load dataset once into session_state
@st.cache_data
def load_data():
    return pd.read_csv(f"d:/Study_Unimi/Coding_Python/Project_2025/My_project_DSE_2025/Dataset/songs_cleaned.csv")

if "df" not in st.session_state:
    st.session_state["df"] = load_data()

st.title(" The Emotion of Sound")
st.write("""
Chào mừng bạn đến dashboard phân tích âm nhạc!  
Hãy chọn một trang ở bên trái để bắt đầu khám phá.
""")