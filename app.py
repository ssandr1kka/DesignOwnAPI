from flask import Flask, render_template, request, jsonify
from model import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:159753@localhost:5432/test2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight")
    flight.add_passenger(name)
    return render_template("success.html")


@app.route("/flights")
def flights():
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flights")
    passengers = flight.passengers
    return render_template("flight.html", flight=flight, passengers=passengers)


@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"Error": "Invalid flight_id"}), 422

    passengers = flight.passengers
    name = []
    for passenger in passengers:
        name.append(passenger.name)
    return jsonify({
        "origin": flight.origin,
        "destination": flight.destination,
        "duration": flight.duration,
        "passenger": name
    })
