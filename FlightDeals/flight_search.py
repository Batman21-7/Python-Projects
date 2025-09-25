import requests
import datetime as dt


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        # self.API_KEY = "passWrvGUUCKTMWcjOoIVgtcXijmRYEElMyr"
        self.ENDPOINT = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": "WrvGUUCKTMWcjOoIVgtcXijmRYEElMyr"
        }

    def get_city_code(self, city):
        params = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=f"{self.ENDPOINT}/locations/query", headers=self.headers, params=params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search(self, end, max_price):
        tomorrow = dt.datetime.now() + dt.timedelta(days=1)
        end_date = dt.datetime.now() + dt.timedelta(days=182)
        params = {
            "fly_from": "LON",
            "fly_to": end,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": end_date.strftime("%d/%m/%Y"),
            "price_to": max_price,
            "curr": "GBP",
            "limit": 5
        }
        response = requests.get(url=f"{self.ENDPOINT}/v2/search", headers=self.headers, params=params)
        return response.json()
