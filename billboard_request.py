import requests
import json
from pprint import pprint

billboard_url = "https://billboard-api2.p.rapidapi.com/year-end-chart/hot-100-songs"
params = {"year":"2023"}
headers = {
	"x-rapidapi-key": "65155348c9mshaa21262afddd264p14c37bjsn21ec97b632c2",
	"x-rapidapi-host": "billboard-api2.p.rapidapi.com"
}

billboardresponse = requests.get(billboard_url, headers=headers, params=params).json()

test_song = billboardresponse["content"]["1"]






song_id_dictionary = []

for song in song_dictionary:
    songtitle = song
    artist = song_dictionary[song]

    search_url = f"https://api.spotify.com/v1/search?q=track%3A{songtitle}+artist%3A{artist}&type=track"

    search_response = requests.get(search_url, headers = spotify_headers).json()
    # song_id_dictionary[song] = search_response["tracks"]["items"][0]["id"]
    # no clue why this doesn't work