import streamlit as st
import pandas as pd
from source_code import processing

@st.cache_data
def load_data():
    return pd.read_csv("d:/Study_Unimi/Coding_Python/Project_2025/My_project_DSE_2025/Dataset/songs_cleaned.csv")

# -----------------------------
# INIT SESSION STATE
# -----------------------------
if "df" not in st.session_state:
    st.session_state["df"] = load_data()

df = st.session_state["df"]

st.subheader("Genre Analysis")


df = st.session_state["df"]
fig = processing.songs_per_year(df)
st.pyplot(fig)
