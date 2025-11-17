import pandas as pd

def clean_data(path, file_name_read, file_name_save):
    # Read data file
    df = pd.read_csv(path + file_name_read)

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
    df["energy_level"] = pd.cut(df["energy"], bins=[0, 0.4, 0.7, 1.0],labels=["Low", "Medium", "High"])

    df["artist"] = df["artist"].str.strip().str.lower()

    # Normalize genre
    df["genre"] = df["genre"].str.lower().str.replace("-", " ").str.strip()

    # genre column has more than 1 value (hip hop, pop, R&B) so we need to split (take first tag only)
    df["genre_main"] = df["genre"].apply(lambda x: x.split(",")[0].strip())

    # change set() value to Unknown
    df['genre_main'] = df['genre_main'].replace('set()', 'unknown')

    # Save data in new file
    df.to_csv(path + file_name_save, encoding='utf-8', index=False, header=True)
    print("Cleaned data saved to new file")
    return df
