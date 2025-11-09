import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

def clean_data(path):
    # Read data file
    df = pd.read_csv(path)

    # Drop duplicates & missing
    df = df.drop_duplicates(subset=["song", "artist", "year"])
    df = df.dropna(subset=["year", "danceability", "energy"])
    
    # Filter year range
    df = df[(df["year"] >= 1960) & (df["year"] <= 2024)]

    # Add Decade column
    df["decade"] = (df["year"] // 10) * 10

    # Add duration_min column
    df["duration_min"] = df["duration_ms"] / 60000

    # Add energy_level column
    df["energy_level"] = pd.cut(df["energy"],
                                bins=[0, 0.4, 0.7, 1.0],
                                labels=["Low", "Medium", "High"])
    # Normalize genre
    df["genre"] = df["genre"].str.lower().str.replace("-", " ").str.strip()

    # Clean up genre combinations (take first tag only)
    # df["genre_main"] = df["genre"].apply(lambda x: x.split(",")[0].strip())


    # Save data in new file
    df.to_csv("Dataset/songs_cleaned.csv", encoding='utf-8', index=False, header=True)
    print("Cleaned data saved to new file")
    return df
