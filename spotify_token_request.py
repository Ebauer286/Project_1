"""
Notes on use: create a .py file and name it 'spotify_credentials'. In the file, create two variables named "client_id" and "client_secret". Save your Spotify ID and Secret code in these variables, as strings.

Follow instructions here to get the Client ID and Client Secret:
https://developer.spotify.com/documentation/web-api/tutorials/getting-started

"""


import requests
import json
from spotify_credentials import client_id, client_secret
from pprint import pprint

url = "https://accounts.spotify.com/api/token"
header = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"grant_type":"client_credentials",
        "client_id" : client_id,
        "client_secret" : client_secret}

r = requests.post(url, data=data, headers=header).json()

pprint(r)
