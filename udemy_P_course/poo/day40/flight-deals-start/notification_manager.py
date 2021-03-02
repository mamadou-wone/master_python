import requests
import smtplib
from twilio.rest import Client
ACCOUNT_SID = ""
AUTH_TOKEN = ""
MY_EMAIL = ""
MY_PASSWORD = ""
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_message(self, message):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
                        .create(
                                body=f"{message}",
                                from_="+17039409833",
                                to="+221774724175"
                        )
        print(message.status)


    def send_email(self, to_email, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=f"{to_email}",
                           msg=f"Subject:Flight Price Alert ! \n\n{message}"
                           )
