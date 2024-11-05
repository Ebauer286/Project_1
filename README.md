# Project 1: Analyzing Trends in Popular Music from 1980 to Present Day.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Data Preprocessing](#data-preprocessing)
- [Limitations](#limitations)
- [Analysis and Conclusions](#analysis-and-conclusions)
- [License](#license)
  
## Project Overview
This project analyzes music trends from the 1980s to the present day using data sourced from Spotify and Billboard, with the objective to uncover and analyze trends in musical characteristics such as danceability, tempo, energy, loudness, valence, duration, key, time signature, and explicit content, to answer some questions like: 
what is popular music trending more towards? Is popular music getting faster? Are popular songs getting longer? Is popular music getting more or less complex/diverse? Is popular music becoming more explicit? What trends popular music would we highlight to music executives looking to publish the next big hit?

To answer all these questions, we gathered the top 100 songs from each week since January of 1980, collected from the Billboard Hot 100, and evaluated the most recurring songs each year to create our own Top 100 Songs chart for each year. 

## Data Source
The data was retrieved from Spotify and Billboard, which provides a vast amount of data and trends. Details on how the data was accessed and any specific filters applied are documented here.
We collected data from the [Billboard Hot 100 API](https://rapidapi.com/LDVIN/api/billboard-api) and [Spotify's API's](https://developer.spotify.com/documentation/web-api) for this project.

### API Call:
- (https://rapidapi.com/LDVIN/api/billboard-api)
- (https://developer.spotify.com/documentation/web-api)
  
## Technologies Used
- Programming Languages: Python
- Data Analysis Libraries: Pandas
- Visualization: Matplotlib
- APIs: (https://developer.spotify.com/documentation/web-api) and (https://rapidapi.com/LDVIN/api/billboard-api)
- Other: Jupyter Notebook, requests (for API data fetching)

## Setup and Installation
1. Clone the repository:
```bash
git clone https://github.com/Ebauer286/Project_1.git
```
2. Navigate to the project directory
cd music-trend-analysis
3. Install dependencies:
```bash
pip install -r requirements.txt
```
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
4. Aproximately two dozen song ID's could not be found when cross referencing the Billboard to the Spotify lists and therefore were removed from the data set.
5. When making our Top 100 songs for each year, we totaled how many weeks the song charted for only that year, which disregards songs that might chart for many weeks, but did so across multiple years. Therefore, the Top 100 Songs we gathered for each year might not be fully representative of the most "popular" music.

## Analysis and Conclusions
Analysis and conclusions can all be found in [Project_1_Final_Write-Up.ipynb](https://github.com/Ebauer286/Project_1/blob/main/Project_1_Final_Write-Up.ipynb)

## License
