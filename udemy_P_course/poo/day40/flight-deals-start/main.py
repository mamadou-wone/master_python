import requests
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime
from data_manager import DataManager
from flight_data import FlightData
from sheety_data import SheetyData

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
SHEET_API_KEY = ""

sheet_data = SheetyData()


def add_user():
    print("Welcome to Boss's Flight Club.\n"
          "We find the best flight deals and email you.")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email?\n")
    confirm_email = input("Type your email again\n")

    if email == confirm_email:
        sheet_data.post_data(first_name, last_name, email)
    else:
        print("Check your email input")


# add_user()
data_email = sheet_data.get_element()
# print(email)


data_manager = DataManager(SHEET_API_KEY)

sheet_data = data_manager.get_data()['prices']
flight_data = FlightData()
# print(flight_data.api_call("PAR"))

# for data in sheet_data:
#     if data['iataCode'] == "":
#         flight_search = FlightSearch(data['city'])
#         data_manager.update_sheet(data['id'], flight_search.city)


notification = NotificationManager()

for data in sheet_data:
    try:
        price = flight_data.api_call(data['iataCode'])
        for lowest in price:
            # print(lowest['cityTo'])
            if data['lowestPrice'] > lowest['price']:
                for email in data_email:
                    notification.send_email(email['email'],
                                            f"Low price alert! Only ${lowest['price']} to fly from "
                                            f"{lowest['cityFrom']}-{lowest['flyFrom']}"
                                            f" to {lowest['cityTo']}-{lowest['flyTo']}"
                                            f" from {datetime.now().date()} to "
                                            f"{lowest['utc_departure'].split('T')[0]}"
                                            )
            break
    except KeyError:
        continue

    # notification.send_message(
    #     f"Low price alert! Only ${lowest['price']} to fly from "
    #     f"{lowest['cityFrom']}-{lowest['flyFrom']}"
    #     f" to {lowest['cityTo']}-{lowest['flyTo']}"
    #     f" from {datetime.now().date()} to "
    #     f"{lowest['utc_departure'].split('T')[0]}"
    # )
