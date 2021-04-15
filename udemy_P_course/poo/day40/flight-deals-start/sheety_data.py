import requests
API_KEY = "3d0f05f887e0580677d4c0878ad2d460"
API_END_POINT = "https://api.sheety.co/"
OPTION = "flightDeals/users"
class SheetyData:
    # def __init__(self):


    def get_element(self):
        response = requests.get(f"{API_END_POINT}{API_KEY}/{OPTION}")
        # print(response.json())
        return response.json()['users']
    # {'users': [{'firstName': 'test', 'lastName': 'test', 'email': 'tes', 'id': 2}]}

    def post_data(self, first_name, last_name, email):
        sheet_header = {
            "Content-Type": "application/json"
        }
        new_row = {
            "user": {
                "firstName": f"{first_name}",
                "lastName": f"{last_name}",
                "email": f"{email}"
            }
        }
        response = requests.post(f"{API_END_POINT}{API_KEY}/{OPTION}", json=new_row,
                                 headers=sheet_header
                                 )
        print(response.text)