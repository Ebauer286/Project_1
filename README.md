We collected data from the Top 100 Billboard API (https://rapidapi.com/LDVIN/api/billboard-api) and Spotify API's for this project. (https://developer.spotify.com/documentation/web-api) 

This project evaluates song metrics, leveraging the Billboard Hot100 API and Spotify Web API. 

The top 100 songs per week collected and combined to create lists of top 100 (i.e. most popular) songs per year. For the purposes of this project, the 'most popular' is defined as frequency of appearance in Billboard weekly top 100 song lists. For example if song A appears in 20 out of 52 top 100 weekly lists, and song B appears in 22 out of 52 top 100 weekly lists, then song A is more popular.






All analysis conclusions are drawn within the parameters of Spotify data. 



Limitations:
- We were unable to find a working API to collect Genre data. While we could succesfully draw many conclusions from the API's we did have access to, having genre data would have allowed us to be more thorough and allow for deeper comparisons such as how the change in loudness of music differed over the decades with the change of popularity in certain genres.

- The following weeks did not have Billboard data and were therefore not included:
    - 1984-02-18
    - 1989-03-11
 
- Some songs at the end of the Top 100 lists had ties therefore some songs were cut off in favor of the first song to hit the lowest count on the top 100.
- Aproximately two dozen song ID's could not be found when cross referencing the Billboard to the Spotify lists and therefore were removed from the data set