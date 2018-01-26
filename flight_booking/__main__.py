import click
from flight_booking.find_and_book import FindAndBookFlight


@click.command()
@click.option('--from', 'from_location', required=True, help="IATA code of departure airport")
@click.option('--to', "to_location", required=True, help="IATA code of arrival airport")
@click.option('--date', "date", required=True, help="Date of the trip (yyyy-mm-dd)")
def runner(from_location, to_location, date):
    book = FindAndBookFlight()
    print(book.find_flight(from_location, to_location, date))


runner()

