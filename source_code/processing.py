import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# def number song per year
def songs_per_year (df: pd.DataFrame):
    """
    Number of songs per year
    """
    songs_per_years = df['year'].value_counts().sort_index()
    plt.bar(df['year'], songs_per_years)
    plt.title("Number of songs per year")
    plt.show()



# TRENDS OVER TIME
def trend_over_time(df: pd.DataFrame):
    """
    Show trend of music over time
    """
    features = ["danceability", "energy", "acousticness", "valence"]
    df_decade = df.groupby("decade")[features].mean().reset_index()

    plt.figure(figsize=(10, 6))
    for f in features:
        sns.lineplot(x = "decade", y = f, data = df_decade, label = f, linewidth = 2)
    plt.title("Evolution of Audio Features by Decade", fontsize = 14)
    plt.xlabel("Decade")
    plt.ylabel("Average Feature Value")
    plt.legend()
    plt.show()

