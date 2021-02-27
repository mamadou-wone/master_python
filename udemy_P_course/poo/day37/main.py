import requests
from datetime import datetime

USERNAME = "mwone"
TOKEN = "maimounaleau"
GRAPH_ID = "maimouna"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameter = {
    "token": "maimounaleau",
    "username": "mwone",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameter)
# response.raise_for_status()
# print(response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameter = {
    "id": "maimouna",
    "name": "boss",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_graph_endpoint, json=graph_parameter, headers=headers)
# print(response.text)

post_value = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date = datetime.today().date().strftime("%Y%m%d")

# print(type(date))
graph_post_param = {
    "date": f"{date}",
    "quantity": "105"
}

# response = requests.post(url=post_value, headers=headers, json=graph_post_param)
# print(response.text)

update_value = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

update = {
    "quantity": "8",
    "unit": "km",
    "color": "ajisai"
}

# response = requests.put(url=update_value, json=update_value, headers=headers)
# print(response.text)

response = requests.delete(url=update_value, headers=headers)
print(response.text)