import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    return pd.read_csv("d:/Study_Unimi/Coding_Python/Project_2025/My_project_DSE_2025/Dataset/songs_cleaned.csv")

# -----------------------------
# INIT SESSION STATE
# -----------------------------
if "df" not in st.session_state:
    st.session_state["df"] = load_data()

df = st.session_state["df"]
print(df)
st.title("Phân Tích Energy Level")

df["energy_level"] = pd.cut(
    df["energy"],
    bins=[0, 0.4, 0.7, 1.0],
    labels=["Low", "Medium", "High"]
)

genre_energy = df.groupby(["genre_main", "energy_level"]).size().reset_index(name="count")

fig, ax = plt.subplots(figsize=(12,6))
sns.barplot(data=genre_energy, x="genre_main", y="count", hue="energy_level", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
