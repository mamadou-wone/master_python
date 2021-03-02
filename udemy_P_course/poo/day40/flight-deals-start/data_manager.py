import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, api_key):
        self.api_key = api_key
        self.response = requests.get(f"https://api.sheety.co/{self.api_key}/flightDeals/prices")
    def get_data(self):
        return self.response.json()

    def update_sheet(self, row_id, new_row={},):
        sheet_header = {
            "Content-Type": "application/json"
        }
        self.response = requests.put(url=f"https://api.sheety.co/3d0f05f887e0580677d4c0878ad2d460/flightDeals/prices/{row_id}",
                                     json=new_row, headers=sheet_header
                                     )
        print(self.response.text)
