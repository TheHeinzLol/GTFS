import json
from pathlib import Path
import requests 


def fetch_response(service: str = "trip_updates") -> requests.models.Response:
    """Checks connection to endpoint.
    Args: 
        service:
            'trip_updates'- updates every 15 seconds on the api server.
            Redundant due to vehicle_position being available. I've found no use of it.
            'vehicle_positions' - updates every second. 
            'service_alerts' - updates once every 5 minutes"""
    # Read credentials
    credentials_path = Path("./config/digitransit_keys.json")
    with open(credentials_path, mode="r", encoding="utf-8" ) as credentials_json:
        credentials = json.load(credentials_json)
    # Endpoints
    endpoints = {
            "service_alerts": f"https://realtime.hsl.fi/realtime/service-alerts/v2/hsl?digitransit-subscription-key={credentials['primary_key']}",
            "vehicle_positions": f"https://realtime.hsl.fi/realtime/vehicle-positions/v2/hsl?digitransit-subscription-key={credentials['primary_key']}",
            "trip_updates": f"https://realtime.hsl.fi/realtime/vehicle-positions/v2/hsl?digitransit-subscription-key={credentials['primary_key']}"
            }
    # vehicle_positions
    try:
        response = requests.get(service)
        response.raise_for_status()
        print("API response received successfully.")
        return response

    except: requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        raise

if __name__ = "__main_":
    fetch_response()
