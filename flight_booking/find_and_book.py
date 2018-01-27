import requests
from .utils import Utils
import time
import json


class FindAndBookFlight:

    def __init__(self, bags):
        self.find_flight_url = "https://api.skypicker.com/flights?"
        self.check_flights_url = "https://booking-api.skypicker.com/api/v0.1/check_flights?"
        self.book_flight_url = "http://128.199.48.38:8080/booking"
        self.headers = {"Content-type": "application/json"}
        self.utils = Utils()
        self.bags = bags
        self.pap = {"lang":"en",
                    "bags": bags,
                    "passengers":[
                        {
                            "lastName":"Klika",
                            "cardno":None,
                            "birthday":"1999-03-03",
                            "phone":"123456",
                            "nationality":"CZ",
                            "firstName":"Franta",
                            "expiration":None,
                            "email":"a@a.aa",
                            "title":"Mr",
                            "documentID": "123456"
                        }
                    ],
                    "locale":"en",
                    "currency":"CZK",
                    "affily":"affil_id",
                    "booked_at":"affil_id"}

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
        booking_token = response.json()['data'][0]["booking_token"]
        return booking_token

    def check_flight(self, booking_token, bags):
        """
        Checks whether the chosen flight can be booked.
        :return: True/False
        """

        querystring = {"v": 2,
                       "booking_token": booking_token,
                       "bnum": bags,
                       "pnum": 1}

        response = requests.request("GET", self.check_flights_url, headers=self.headers, params=querystring)
        flights_checked = response.json()['flights_checked']
        flights_invalid = response.json()['flights_invalid']
        return flights_checked, flights_invalid

    def repeat_until_checked(self, booking_token, bags):
        flight_invalid = False
        flights_checked = False
        while flights_checked is not True:
            flights_checked, flight_invalid = self.check_flight(booking_token, bags)
            if not flights_checked:
                time.sleep(5)
        if flight_invalid:
            print("Flight cannot be booked. Please try another flight.")
            exit()

    def book_flight(self, booking_token):

        self.pap["booking_token"] = booking_token
        response = requests.request("POST", self.book_flight_url, data=json.dumps(self.pap), headers=self.headers)
        return response.json()


