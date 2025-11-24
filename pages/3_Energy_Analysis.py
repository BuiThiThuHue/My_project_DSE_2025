import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
st.title("Energy Level Analyst")

# ===== SIDEBAR FILTER ======================================================

st.sidebar.header("Energy level")

selected_levels = st.sidebar.multiselect(
    "select level:",
    options= df["energy_level"].unique(),
    default= []
)

if selected_levels:
    df_filtered = df[df["energy_level"].isin(selected_levels)]
else:
    df_filtered = df


#----Total songs
if selected_levels:
    st.write(f"Total songs in {', '.join(selected_levels)} energy level: {len(df_filtered)} songs")
else:
    st.write(f"Total songs in ALL energy level: {len(df_filtered)} songs")
st.markdown("---")

# Number songs by Energy Level
st.markdown("## Songs by Energy Level")

fig = processing.song_per_enery(df_filtered)
st.pyplot(fig)

st.markdown("---")

# plot ENERGY by year
st.markdown("## Trend of Energy over year")

energy_year = df_filtered.groupby("year")["energy"].mean().reset_index()
energy_year["year"] = energy_year["year"].astype(int)

fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(data=energy_year, x="year", y="energy", ax=ax, marker="o")
ax.set_title("Average Energy Over Time")
st.pyplot(fig)

st.markdown("---")

# trend Energy Level over decade
st.markdown("##  Trend of Energy Level over decade")
fig1 = processing.trend_of_energy(df)
st.pyplot(fig1)

st.markdown("---")