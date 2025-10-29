from source_code.clean_data import clean_data
# Load and clean data
df = clean_data("Dataset/songs_normalize.csv")

print(df.head())
