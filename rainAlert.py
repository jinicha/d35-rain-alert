import requests
import config
from twilio.rest import Client

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
    account_sid = config.account_sid
    auth_token = config.auth_token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It is going to rain, remember to bring an umbrella :)",
        from_=config.send_from,
        to=config.send_to
    )

    print(message.status)