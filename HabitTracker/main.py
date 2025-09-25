import requests
import datetime as dt

TOKEN = "Batman217"
USERNAME = "batman217"

headers = {
    "X-USER-TOKEN": TOKEN
}

# params = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "sora"
# }
#
# response = requests.post(url="https://pixe.la//v1/users/batman217/graphs", json=params, headers=headers)
# print(response.text)

today = dt.datetime.now()


def create(quantity):
    params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": quantity
    }

    response = requests.post(url="https://pixe.la//v1/users/batman217/graphs/graph1", json=params, headers=headers)
    print(response.text)


def update(date, quantity):
    params = {
        "quantity": quantity
    }

    response = requests.put(url=f"https://pixe.la//v1/users/batman217/graphs/graph1/{date}", json=params, headers=headers)
    print(response.text)
