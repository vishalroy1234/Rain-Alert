import requests
from twilio.rest import Client

account_sid = "ACb8881f1d8e465828f59751f7c1b1a402"
auth_token = "4fca1bb9bfbadad6e0c35f80c9aa05dc"


parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": "7a734f9528aa732bada6d734ded1e57b",
    "exclude": "current,minutely,daily,alerts",
    "units": "metric",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_ids = []
for hour in range(12):
    weather_ids.append(data['hourly'][hour]['weather'][0]['id'])
print(weather_ids)
for id in weather_ids:
    print(id)
    if id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Its going to rain today. Remember to bring an ☂️",
            from_='+18329254054',
            to='Your phone number'
        )

        print(message.status)
        break
