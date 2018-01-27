from datetime import datetime

# TODO implement logger for debugging
# TODO handle exceptions


class BookFlightErrors(Exception):
    """Base class for exceptions in flight_booking"""
    pass


class InputError(BookFlightErrors):
    """Raise when there is an error on input"""

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class Utils:

    def skypicker_api_date_format_convertor(self, date):
        """
        Reformats entered date to Skypicker's api date format

        :param date: Date entered by user in yyyy-mm-dd format
        :return: Skypicker's api date format in dd/mm/yyyy format
        """

        try:
            return datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        except ValueError:
            message = "Invalid date {}".format(date)
            raise InputError(date, message)
