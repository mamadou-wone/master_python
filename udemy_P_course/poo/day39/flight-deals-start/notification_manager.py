import requests
from twilio.rest import Client
ACCOUNT_SID = "AC2f66923cc89ca72ea11f17a038d02c85"
AUTH_TOKEN = "bf61f67c06df94e909ff2ed9b4801f64"
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