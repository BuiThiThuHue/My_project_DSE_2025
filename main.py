from source_code import clean_data
from source_code import processing
# Load and clean data
file_name_read = "songs_data.csv"
file_name_save = "songs_cleaned.csv"
data_path = f'd:/Study_Unimi/Coding_Python/Project_2025/My_project_DSE_2025/Dataset/'
df = clean_data.clean_data( data_path,file_name_read,file_name_save)   

print(df.shape)

processing.songs_per_year(df)

# processing.plot_trend_over_time(df)
