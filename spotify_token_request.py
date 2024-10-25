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
