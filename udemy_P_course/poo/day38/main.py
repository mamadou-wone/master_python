import requests
from datetime import datetime

APP_ID = "de90e36e"
API_KEY = "f9b5a3498d7d1fa4fa5d8ab989532b7b"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercice = input("Tell us Which Exercice you did: ")

query = {
 "query": f"{exercice}",
 # "gender": "female",
 # "weight_kg": 72.5,
 # "height_cm": 167.64,
 # "age": 30
}


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=nutritionix_endpoint, json=query, headers=headers)
data = response.json()


SHEET_KEY = "3d0f05f887e0580677d4c0878ad2d460"
PROJECT_NAME = "workoutTracking"
SHEET_NAME = "workouts"
sheet_endpoint = "https://api.sheety.co/3d0f05f887e0580677d4c0878ad2d460/workoutTracking/workouts"
# Ran 5k and cycled for 20 minutes.
sheet_header = {
    "Content-Type": "application/json"
}

date = datetime.now().date()
time = datetime.now().time().strftime("%H:%M:%S")

# print(time)

new_row = {
    "workout": {
        "date": f"{date}",
        "time": f"{time}",
        "exercise": f"{data['exercises'][0]['name']}",
        "duration": f"{data['exercises'][1]['duration_min']}",
        "calories": f"{data['exercises'][1]['nf_calories']}"
    }
}


test = requests.post(url=sheet_endpoint, json=new_row, headers=sheet_header)
print(test.text)