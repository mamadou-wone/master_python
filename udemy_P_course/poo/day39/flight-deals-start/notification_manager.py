import requests
from twilio.rest import Client
ACCOUNT_SID = ""
AUTH_TOKEN = ""
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