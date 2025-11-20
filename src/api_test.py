#from google.transit import gtfs_realtime_pb2
import json
from pathlib import Path
import requests 

# Read credentials
credentials_path = Path("./digitransit_keys.json")
with open(credentials_path, mode="r", encoding="utf-8" ) as credentials_json:
    credentials = json.load(credentials_json)

url = f"https://realtime.hsl.fi/realtime/vehicle-positions/v2/hsl?digitransit-subscription-key={credentials['primary_key']}"
response = requests.get(url)
print(response.content)

#feed = gtfs_realtime_pb2.FeedMessage()
#feed.ParseFromString(response.content)
#for entity in feed.entity:
#  if entity.HasField('trip_update'):
#    print(entity.trip_update)

