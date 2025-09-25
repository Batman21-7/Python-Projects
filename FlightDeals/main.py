# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

FlightData = FlightData()
DataManager = DataManager()
Search = FlightSearch()
NotificationManager = NotificationManager()

sheet_data = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
              {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
              {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
              {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
              {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
              {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
              {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
              {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
              {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]   # DataManager.get_data()

cities = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul',
          'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town']  # [i["city"] for i in sheet_data]

codes = ['PAR', 'BER', 'TYO', 'SYD', 'IST', 'KUL', 'NYC', 'SFO', 'CPT']  # [Search.get_city_code(city) for city in
# cities]
# for i in range(len(codes)):
#     DataManager.add_code(codes[i], i+2)

flights = [Search.search(codes[i], sheet_data[i]["lowestPrice"])["data"] for i in range(len(codes))]
# print(flights)
for flight in flights:
    for data in flight:

        message = (f"Only £{data['price']} to fly from {data['cityFrom']}-{data['flyFrom']} to "
             f"{data['cityTo']}-{data['flyTo']}, "
             f"from {data['local_departure'].split('T')[0]} to {data['local_arrival'].split('T')[0]}")

        NotificationManager.send_notification(message)
