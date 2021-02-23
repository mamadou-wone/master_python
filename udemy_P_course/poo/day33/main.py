import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
#
# data = response.json()
# print(data['iss_position'])
MY_LAT = 14.716677
MY_LNG = -17.467686
parameter = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameter)

response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
print(sunrise.split("T")[1].split(":"))

for i in range(46, 56):
    print(i)