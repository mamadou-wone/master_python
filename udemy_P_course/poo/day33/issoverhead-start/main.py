import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 14.716677
MY_LONG = -17.467686

def current_position(lat, lgn):
    best_position = False
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    lat_error = lat - 5
    lat2_error = lat + 5
    lng_error = lgn - 5
    lng2_error = lgn + 5
    if iss_latitude >=lat_error and iss_latitude <= lat2_error and iss_longitude >= lng_error and iss_longitude <= lng2_error:
        best_position = True
    return best_position
#Your position is within +5 or -5 degrees of the ISS position.





positon = current_position(MY_LAT, MY_LONG)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
sunrise_hour = time_now.hour
# print(sunrise_hour)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.





def send_mail():
    if positon and sunrise_hour == sunrise:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="megawone735@gmail.com", password="775596731")
            connection.sendmail(from_addr="megawone735@gmail.com", to_addrs="m.wone735@yahoo.com",
                                msg="Subject:Look\n\nHello boss look"
                                )

def timer(start):
    for i in range(start):
        time.sleep(1)
        start -= 1
        print(start)
        if start == 0:
            send_mail()
            start = 60
            timer(start)


timer(60)