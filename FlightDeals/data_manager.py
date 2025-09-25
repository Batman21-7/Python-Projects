import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.SHEET_ENDPOINT = "https://api.sheety.co/0da5a2c410982385790785c29ca4d0c2/flightDeals/prices"
        self.TOKEN = "456yhko%uy$dey3e2xn@"
        self.headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {self.TOKEN}"
        }

    def get_data(self):
        response = requests.get(url=self.SHEET_ENDPOINT, headers=self.headers)
        return response.json()["prices"]

    def add_code(self, city_code, num):
        json = {
            "price": {
                "iataCode": city_code
            }
        }
        response = requests.put(url=f"{self.SHEET_ENDPOINT}/{num}", headers=self.headers, json=json)
