import click
from flight_booking.find_and_book import FindAndBookFlight

# TODO implement all parametres
# TODO write documentation


@click.command()
@click.option('--from', 'from_location', required=True, help="IATA code of departure airport")
@click.option('--to', "to_location", required=True, help="IATA code of arrival airport")
@click.option('--date', "date", required=True, help="Date of the trip (yyyy-mm-dd)")
@click.option('--bags', 'bags', default=0, help="Number of bags to book")
def runner(from_location, to_location, date, bags):
    find_and_book = FindAndBookFlight(bags)
    booking_token = find_and_book.find_flight(from_location, to_location, date)

    find_and_book.repeat_until_checked(booking_token, bags)

    response = find_and_book.book_flight(booking_token)

    if response["status"] == "confirmed":
        print("Booking succesful: ", response["pnr"])
    else:
        print("Flight cannot be booked")


runner()

