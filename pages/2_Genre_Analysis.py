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

# st.header("Genre Analysis")


# --- Sidebar Filters ---
st.sidebar.header("Genre")
selected_genres = st.sidebar.multiselect(
    "Select Genre:",
    options=df["genre_main"].unique(),
    default=[]
)

if selected_genres:
    df_filtered = df[df["genre_main"].isin(selected_genres)]
else:
    df_filtered = df

#----Total songs
if selected_genres:
    st.write(f"Total songs in genres {', '.join(selected_genres)}: {len(df_filtered)} songs")
else:
    st.write(f"Total songs in ALL genres: {len(df_filtered)} songs")

st.markdown("---")

# -------------------------------------------------------------------
# Phân bố số bài hát theo thể loại
st.markdown("## Songs by genre")
fig = processing.song_per_genre(df_filtered)
st.pyplot(fig)

st.markdown("---")

#-------------
st.markdown("## Top 5 genres by decade")
top_genre = processing.top_genre_songs(df_filtered)
fig = processing.plot_top_genre(top_genre)
st.pyplot(fig)
st.markdown("---")

# Energy Level theo Genre
st.markdown("## Energy Level by Genre")
fig = processing.plot_Energy_Genre(df_filtered)
st.pyplot(fig)