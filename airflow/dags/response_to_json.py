#too early for that. to s3 bronze first
from google.transit import gtfs_realtime_pb2
import json
from pathlib import Path

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)
    for entity in feed.entity:
        print(entity)
