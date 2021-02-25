from twilio.rest import Client


import requests

account_sid = ""
auth_token = ""




api_key = ""
api_url = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 14.6937,
    "lon": -17.4441,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(api_url, params=parameters)
response.raise_for_status()

data = response.json()

weather_slice = data["hourly"][:12]

will_rain = False

for hour in weather_slice:
    if int(hour["weather"][0]["id"]) <= 800:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hello Boss",
        from_='+14159675282',
        to='+221774724175'
    )

    print(message.status)