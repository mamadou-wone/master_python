API_END_POINT = "https://tequila-api.kiwi.com/v2/search"
API_KEY = "lF0WWXaoTtIOuwkSUpbwjnhI6szex8fr"
import requests
from datetime import datetime, timedelta
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        # self.price
        # self.departure_airport_code
        # self.departure_city
        # self.response
        pass



    def api_call(self, city_code):
        date = datetime.now().date() + timedelta(days=1)
        six_month_later = date + timedelta(days=180)
        headers = {
            "apikey": API_KEY,
        }

        parameter = {
            "fly_from": "LON",
            "fly_to": f"{city_code}",
            "date_from": f"{date.strftime('%d/%m/%Y')}",
            "date_to": f"{six_month_later.strftime('%d/%m/%Y')}"
        }

        response = requests.get(url=API_END_POINT, params=parameter, headers=headers)
        data = response.json()
        return data['data']

