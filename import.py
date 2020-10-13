import csv

from flask import Flask
from model import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:159753@localhost:5432/test2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        print(f"Flight from {flight.origin} to {flight.destination}, duration {flight.duration} minutes")
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        main()
