# Project 1: Analyzing Trends in Popular Music from 1980 to Present Day

## Table of Contents
- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Data Preprocessing](#data-preprocessing)
- [Analysis and Findings](#analysis-and-findings)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [License](#license)
  
## Project Overview
This project analyzes music trends from the 1980s to 2024 using data sourced from [Music API Name]. Key goals:

Identify trends in popular genres over time.
Analyze the evolution of metrics like tempo, key, duration, and popularity.
Explore the impact of historical and cultural events on music trends.

## Data Source
The data was retrieved from [Music API Name], which provides a vast amount of data on songs, artists, genres, and trends. Details on how the data was accessed and any specific filters applied are documented here.
We collected data from the Top 100 Billboard API (https://rapidapi.com/LDVIN/api/billboard-api) and Spotify API's for this project. (https://developer.spotify.com/documentation/web-api) 

### API Call:

## Technologies Used
-Programming Languages: Python
-Data Analysis Libraries: Pandas, NumPy
-Visualization: Matplotlib, Seaborn
-APIs: [Music API Name]
-Other: Jupyter Notebook, requests (for API data fetching)
-This project evaluates song metrics, leveraging the Billboard Hot100 API and Spotify Web API. 

## Project Structure
project-root/
│
├── data/                # Raw data from API
├── notebooks/           # Jupyter notebooks for data analysis and visualization
├── src/                 # Python scripts for data extraction and preprocessing
├── README.md            # Project documentation
└── requirements.txt     # Dependencies

## Setup and Installation
1. Clone the repository:
git clone https://github.com/yourusername/music-trend-analysis.git
2. Navigate to the project directory
cd music-trend-analysis
3. Install dependencies:
pip install -r requirements.txt
4. Get an API key from [Music API Name] and add it to your environment variables or config file.

## Data Preprocessing
1. Data was fetched from the API, covering the time range from 1980 to 2024.
2. Preprocessing included handling missing data, filtering outliers, and standardizing genre categories.
3. Saved the cleaned data in data/processed/ for easy access in analysis notebooks.

## Analysis and Findings

## Conclusion
The music landscape has evolved significantly, influenced by both cultural shifts and technological advancements. Key findings and any patterns discovered can be summarized here.
## License

The top 100 songs per week collected and combined to create lists of top 100 (i.e. most popular) songs per year. For the purposes of this project, the 'most popular' is defined as frequency of appearance in Billboard weekly top 100 song lists. For example if song A appears in 20 out of 52 top 100 weekly lists, and song B appears in 22 out of 52 top 100 weekly lists, then song A is more popular.






All analysis conclusions are drawn within the parameters of Spotify data. 



## Limitations:
- We were unable to find a working API to collect Genre data. While we could succesfully draw many conclusions from the API's we did have access to, having genre data would have allowed us to be more thorough and allow for deeper comparisons such as how the change in loudness of music differed over the decades with the change of popularity in certain genres.

- The following weeks did not have Billboard data and were therefore not included:
    - 1984-02-18
    - 1989-03-11
 
- Some songs at the end of the Top 100 lists had ties therefore some songs were cut off in favor of the first song to hit the lowest count on the top 100.
- Aproximately two dozen song ID's could not be found when cross referencing the Billboard to the Spotify lists and therefore were removed from the data set
