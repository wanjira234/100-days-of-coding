import requests
from pprint import pprint


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def data(self):

        self.sheety_endpoint = "https://api.sheety.co/2c7e0fbb73b0d0293e1945cf35b19c26/flightDeals/prices"

        self.prices = {
            "city": "",
            "IATA": "",
            "lowest price": "",
        }
        self.response = requests.get(url=self.sheety_endpoint, json=self.prices)
        pprint(self.response.json())
