import requests
from . import config

API_URL = "https://api.open-meteo.com/v1/forecast"

def get_forecast() -> dict:
    params = {
        "latitude": config.LAT,
        "longitude": config.LON,
        "daily": "temperature_2m_max,precipitation_sum,windspeed_10m_max",
        "timezone": "auto",
        "forecast_days": 1,
    }
    r = requests.get(API_URL, params=params, timeout=15)
    r.raise_for_status()
    d = r.json()["daily"]
    return {
        "max_temp": d["temperature_2m_max"][0],
        "rain": d["precipitation_sum"][0],
        "wind": d["windspeed_10m_max"][0],
    }