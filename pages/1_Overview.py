import streamlit as st
import pandas as pd

from source_code import processing

# -----------------------------
# LOAD DATA WITH CACHE
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("d:/Study_Unimi/Coding_Python/Project_2025/My_project_DSE_2025/Dataset/songs_cleaned.csv")

# -----------------------------
# INIT SESSION STATE
# -----------------------------
if "df" not in st.session_state:
    st.session_state["df"] = load_data()

df = st.session_state["df"]

# -----------------------------
st.title("Data overview")
col1, col2, col3 = st.columns(3)

col1.metric("Number of songs", f"{len(df):,}")
col2.metric("Number of artists", df["artist"].nunique())
col3.metric("Number of genres", df["genre_main"].nunique())

st.markdown("---")

st.subheader("Number of Songs over Year")
fig = processing.songs_per_year(df) 
st.pyplot(fig)
st.markdown("---")
# -----------------------------
# Stats
# -----------------------------
with st.expander("### 10 first rows of dataset"):
    st.dataframe(df.head())

with st.expander("### Quick statistics:"):
    st.write(df.describe())
st.markdown("---")

# plot top 10 artist
st.write("### Top 10 artists")
df = st.session_state["df"]
top10 = processing.top10_artist_songs(df)
# st.dataframe(top10)
fig = processing.plot_top_artists(top10)
st.pyplot(fig)
st.markdown("---")

# show artist with songs
selected_artist = st.selectbox("Select an artist", top10['artist'])
artist_songs = df[df['artist'] == selected_artist]
df2 = artist_songs[['artist','song','year','genre_main','popularity']]
df2 = df2.reset_index(drop=True).sort_values(by="year", ascending=True)
st.dataframe(df2)

st.markdown("---")

# plot trend of feature
st.write("### Feature Trends")
fig2 = processing.plot_trend_over_time(df)
st.pyplot(fig2)