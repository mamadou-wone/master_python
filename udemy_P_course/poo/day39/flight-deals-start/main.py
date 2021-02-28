import requests
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime
from data_manager import DataManager
from flight_data import FlightData
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
SHEET_API_KEY = "3d0f05f887e0580677d4c0878ad2d460"

data_manager = DataManager(SHEET_API_KEY)


sheet_data = data_manager.get_data()['prices']
flight_data = FlightData()
# print(flight_data.api_call("PAR"))

notification = NotificationManager()

for data in sheet_data:
    price = flight_data.api_call(data['iataCode'])
    for lowest in price:
        if data['lowestPrice'] > lowest['price']:
           notification.send_message(
               f"Low price alert! Only ${lowest['price']} to fly from "
               f"{lowest['cityFrom']}-{lowest['flyFrom']}"
               f" to {lowest['cityTo']}-{lowest['flyTo']}"
               f" from {datetime.now().date()} to "
               f"{lowest['utc_departure'].split('T')[0]}"
           )
        break




# for data in sheet_data:
#     if data['iataCode'] == "":
#         flight_search = FlightSearch(data['city'])
#         data_manager.update_sheet(data['id'], flight_search.city)