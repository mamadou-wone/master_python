import requests
API_END_POINT = "https://tequila-api.kiwi.com"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self, city_name):
        self.city_name = city_name
        self.code = self.get_code()
        self.city = {
            "price": {
                "iataCode": self.code,
            }
        }


    def get_code(self):
        headers = {
            "apikey": "lF0WWXaoTtIOuwkSUpbwjnhI6szex8fr"
        }

        parameter = {
            "term": f"{self.city_name}"
        }
        response = requests.get(url=f"{API_END_POINT}/locations/query", params=parameter, headers=headers)
        data = response.json()
        return data['locations'][0]['code']