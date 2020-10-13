import csv

from flask import Flask
from model import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:159753@localhost:5432/test2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    Flights = Flight.query.all()
    for flight in Flights:
        print(f"Flight from {flight.origin} to {flight.destination}, {flight.duration} minutes")


if __name__ == "__main__":
    with app.app_context():
        main()