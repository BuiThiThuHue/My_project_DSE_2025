import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# def number song per year
def songs_per_year (df: pd.DataFrame):
    """
    Number of songs per year
    """
    songs_per_years = df['year'].value_counts().sort_index()
    # print(songs_per_years)

    #create list label
    list_label = []
    for i in songs_per_years.values:
        list_label.append(i)

    #draw bar chart
    bar = plt.bar(songs_per_years.index, songs_per_years.values)
    plt.bar_label(bar, list_label, padding=3)

    #adding title
    plt.title("Number of songs per year")
    plt.xlabel("Years")
    plt.ylabel("Number of songs")
    plt.show()

def top10_artist_songs (df: pd.DataFrame):
    """
    find top 10 Artists with the average popularity of their songs
    """
    artist_df = df[['artist', 'popularity']].groupby('artist').mean().sort_values(by='artist')
    artists = df['artist'].value_counts().sort_index()
    artist_df['total songs'] = artists.values

    artist_df.sort_values(by='total songs',ascending=False, inplace=True)

    artist_df.reset_index(inplace=True)

    df_top10 = artist_df[:10]

    return df_top10

def plot_top_artists(df: pd.DataFrame):
    """
    plot scatter top 10 artists by average popularity of their songs
    """
    plt.figure(figsize=(12, 10))

    # color by popularity
    colors = df['popularity']
    # size by total songs
    sizes = df['total songs'] * 50

    scatter_plot = plt.scatter(df['artist'], df['popularity'], s=sizes, c=colors, cmap='seismic')
    
    # add colorbar
    cbar = plt.colorbar(scatter_plot)
    cbar.set_label('Popularity')

    # make lable for each point
    for i in range(len(df)):
        plt.text(
            df['artist'][i],
            df['popularity'][i] + 0.4,
            f"{df['total songs'][i]} songs",
            ha = 'center',
            fontsize = 9
        )

    plt.title("Top 10 artists by average popularity of their songs")
    plt.xlabel("Artist")
    plt.ylabel("Average Popularity")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


 # trend over time  
def plot_trend_over_time(df: pd.DataFrame):
    features = ["danceability", "energy", "valence", "acousticness"]

    # mean group by decade
    df_decade = df.groupby("decade")[features].mean().reset_index()

    # plot line trend
    plt.figure(figsize=(10, 6))
    for f in features:
        plt.plot(df_decade["decade"], df_decade[f], marker="o", label=f)

    plt.title("Feature Trends by Decade")
    plt.xlabel("Decade")
    plt.ylabel("Mean Value")
    plt.legend()
    plt.tight_layout()
    plt.show() 


def top_genre_songs(df: pd.DataFrame):
    """
    Show top 5 genres by number of song in each decade
    """
    top_genres = df["genre_main"].value_counts().head(5).index
    # print(top_genres)

    df_top = df[df["genre_main"].isin(top_genres)]
    genre_group = df_top.groupby(['decade', 'genre_main']).size().reset_index(name='count')

    genre_pivot = genre_group.pivot(index='genre_main', columns='decade', values='count')
    genre_pivot = genre_pivot.fillna(0)

    return genre_pivot

def plot_top_genre(df: pd.DataFrame):
    """
    Plot top 5 genres by number of song in each decade
    """
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.sort_index(), annot=True, fmt='.0f', cmap='YlGnBu')
    plt.title('Genre Popularity Across Decades')
    plt.xlabel('Decade')
    plt.ylabel('Genre')
    plt.show()

def trend_of_energy(df: pd.DataFrame):
    """
    Trend of Energy Levels over Decades
    """
    energy_trend = df.groupby(["decade", "energy_level"]).size().reset_index(name="count")

    sns.lineplot(
        data = energy_trend,
        x = "decade",
        y = "count",
        hue = "energy_level",
        marker = "v"
    )
    plt.title("Trend of Energy Levels Over Decades")
    plt.show()

def plot_Energy_Genre(df: pd.DataFrame):
    """
    Plot relevant between Energy Level by Genre
    """
    genre_energy = df.groupby(["genre_main", "energy_level"]).size().reset_index(name="count")

    sns.catplot( data = genre_energy, x = "genre_main", y = "count", hue = "energy_level", kind = "bar", height=5, aspect=2)
    plt.xticks(rotation=45)
    plt.title("Energy Level by Genre")
    plt.show()