import requests
import sys



if len(sys.argv) != 2:
    sys.exit("Usage: python songs.py ARTIST")

url = ("https://itunes.apple.com/search?entity=song&limit=10&term=")

data = requests.get(url + sys.argv[1]).json()

for song in data["results"]:
    print(song["trackName"])


