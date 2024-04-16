from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

transportation = Blueprint('transportation', __name__)

# Get all the flights from the database
@transportation.route('/flights', methods=['GET'])
def get_flights():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of flights
    cursor.execute('SELECT flight_no, seats, duration, departure_location, arrival_time, arrival_location, departure_time, airline_name FROM flights')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers.
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Gets all the info for the flight with this flight_no
@transportation.route('/flight/<flight_no>', methods=['GET'])
def get_flights_detail (flight_no):

    query = 'SELECT flight_no, seats, duration, departure_location, arrival_time, arrival_location, departure_time, airline_name FROM flights WHERE flight_no = ' + str(flight_no)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

