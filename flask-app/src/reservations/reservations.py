from flask import Blueprint, request, jsonify, make_response
import json
from src import db

reservations = Blueprint('reservations', __name__)

# Get all the hotels and their info from the database
@reservations.route('/hotel', methods=['GET'])
def get_hotels(): 
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of hotels
    cursor.execute('SELECT hotel_id, amenities, street, city, state, zipcode, duration, rating FROM hotel')

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

# Gets all the restaurants and their info from the database
@reservations.route('/Restaurants', methods=['GET'])
def get_restaurants():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of restaurants
    cursor.execute('SELECT Restaurant_ID, Price, Name, Location FROM Restaurants')

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