# Project 1: Analyzing Trends in Popular Music from 1980 to Present Day.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Data Preprocessing](#data-preprocessing)
- [Limitations](#limitations)
- [Analysis and Findings](#analysis-and-findings)
- [Conclusion](#conclusion)
- [License](#license)
  
## Project Overview
This project analyzes music trends from the 1980s to the present day using data sourced from Spotify and Billboard, with the objective to uncover and analyze trends in musical characteristics such as Danceability, Tempo, Energy, Loudness, Valence, Duration, Key, Time Signature and Explicit Content, to answer some questions like Is popular music trending more towards?, Is popular music getting faster?
Are popular songs getting longer?, Is popular music becoming more explicit?, What trends popular music would we highlight to music executives looking to publish the next big hit?.
to answer all these questions it was use the top 100 songs per week collected and combined to create lists of top 100 (i.e. most popular) songs per year. For the purposes of this project, the 'most popular' is defined as frequency of appearance in Billboard weekly top 100 song lists. For example if song A appears in 20 out of 52 top 100 weekly lists, and song B appears in 22 out of 52 top 100 weekly lists, then song A is more popular.

## Data Source
The data was retrieved from Spotify and Billboard, which provides a vast amount of data and trends. Details on how the data was accessed and any specific filters applied are documented here.
We collected data from the Top 100 Billboard API (https://rapidapi.com/LDVIN/api/billboard-api) and Spotify API's for this project. (https://developer.spotify.com/documentation/web-api) 

### API Call:
- (https://rapidapi.com/LDVIN/api/billboard-api)
- (https://developer.spotify.com/documentation/web-api)
  
## Technologies Used
-Programming Languages: Python
-Data Analysis Libraries: Pandas
-Visualization: Matplotlib
-APIs: (https://developer.spotify.com/documentation/web-api) and (https://rapidapi.com/LDVIN/api/billboard-api)
-Other: Jupyter Notebook, requests (for API data fetching)
-This project evaluates song metrics, leveraging the Billboard Hot100 API and Spotify Web API. 

## Setup and Installation
1. Clone the repository:
git clone https://github.com/Ebauer286/Project_1.git
2. Navigate to the project directory
cd music-trend-analysis
3. Install dependencies:
pip install -r requirements.txt
4. Get the API key from (https://developer.spotify.com/documentation/web-api) and (https://rapidapi.com/LDVIN/api/billboard-api) and add it to your environment variables or config file.

## Data Preprocessing
1. Data was fetched from the API's Spotify and Billboard, covering the time range from 1980 to the present day.
2. Preprocessing included handling missing data, filtering outliers, and standardizing the musical characteristics.
3. Saved the cleaned data in a CSV file for easy access in analysis notebooks.
   
## Limitations:
1. We were unable to find a working API to collect Genre data. While we could succesfully draw many conclusions from the API's we did have access to, having genre data would have allowed us to be more thorough and allow for deeper comparisons such as how the change in loudness of music differed over the decades with the change of popularity in certain genres.
2. The following weeks did not have Billboard data and were therefore not included:
    - 1984-02-18
    - 1989-03-11
3. Some songs at the end of the Top 100 lists had ties therefore some songs were cut off in favor of the first song to hit the lowest count on the top 100.
4. Aproximately two dozen song ID's could not be found when cross referencing the Billboard to the Spotify lists and therefore were removed from the data set

## Analysis and Findings

## Conclusion
All analysis conclusions are drawn within the parameters of Spotify data. 

## License
