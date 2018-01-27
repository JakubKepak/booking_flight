from unittest import TestCase
from flight_booking.utils import Utils
import pytest

# TODO cover the code with tests


class TestUtils(TestCase):

    def test_skypicker_api_date_format_convertor(self):
        utils = Utils()
        assert utils.skypicker_api_date_format_convertor(date="2100-01-01") == "01/01/2100"
