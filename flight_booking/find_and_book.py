import requests
from .utils import Utils


class FindAndBookFlight:

    def __init__(self):
        self.find_flight_url = "https://api.skypicker.com/flights?"
        self.headers = {"Content-type": "application/json"}
        self.utils = Utils()

    def find_flight(self, from_location, to_location, date):

        """
        Finds a flight.
        :return: Booking token for booking the flight
        """

        querystring = {"flyFrom": from_location,
                       "to": to_location,
                       "dateFrom": self.utils.skypicker_api_date_format_convertor(date),
                       "dateTo": self.utils.skypicker_api_date_format_convertor(date),
                       "sort": "duration",
                       "asc": "1"}

        response = requests.request("GET", self.find_flight_url, headers=self.headers, params=querystring)
        response.raise_for_status()
        return response.json()['data'][0]["booking_token"]
