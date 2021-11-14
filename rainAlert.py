import requests
import config

base_url = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": config.lat,
    "lon": config.lon,
    "exclude": "current,minutely,daily,alerts",
    "appid": config.api_key
}

response = requests.get(url=base_url, params=params)
response.raise_for_status()
weather_data = response.json()
next_twelve_hours = weather_data["hourly"][:12]
rain = False
for hour_data in next_twelve_hours:
    code = hour_data["weather"][0]["id"]
    if code < 700:
        rain = True

if rain:
    print("Bring an Umbrella")
