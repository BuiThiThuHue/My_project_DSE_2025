# My_project_DSE_2025
Project for Coding for Data Science and Data Management

# Project target
The Sound of Change: 
* **Target:** Analyzing the changing nature of music over the decades, using Spotify data. This project explores how popular music has changed from the **1980 to 2020**.
* **Web application:** The Streamlit app allows users to interact visually with data, exploring music trends in an easy-to-understand and intuitive way.
# Source Dataset 
The dataset used comes from Kaggle, this is the [link](https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019/data?select=songs_normalize.csv) to download data file.

# Structure of project

* MY_PROJECT_DSE_2025
    * Dataset
        * songs_data.csv
        * songs_cleaned.csv
    * pages
        * 1_Overview.py
        * 2_Genre_Analysis.py
        * 3_Energy_Analysis.py
    * source_code
        * clean_data.py
        * processing.py
        * __init__.py
    * presentation
        * visualization.ipynb
    * requirements.txt
    * main.py
    * Home.py
    * README.md
    * test.ipynb

# Setup environment
pip install -r requirements.txt

# Run pipe line
python main.py

# Run app
streamlit run Home.py
