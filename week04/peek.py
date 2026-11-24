import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python songs.py ARTIST")

url = ("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
response = requests.get(url)
data = response.json()
print(json.dumps(data, indent=2))