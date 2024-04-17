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

# Updates the time at which the reservation is booked at the restaurant with 
# the given Reservation_ID
@reservations.route('/Restaurants_Booked/<Booked_ID>', methods=['PUT'])
def update_restaurant_time(Booked_ID):
    cust_data = request.get_json()

    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Restaurants_Booked SET Datetime=%s WHERE Booked_ID=%s',
                     (cust_data.get('Datetime'), Booked_ID))
    db.get_db().commit()

    return jsonify({'message': 'Restaurant reservation time updated successfully'})

# Gets all the activities and their info from the database
@ reservations.route('/activities', methods=['GET'])
def get_activities():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of activities
    cursor.execute('SELECT activities_id, name, cost FROM activities')

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

# Gets all the room types, their info, and the hotels with the room type from the database
@reservations.route('/room_type', methods=['GET'])
def get_room_types():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of room types
    cursor.execute('SELECT type_id, Name, max_guests, total_room, description, room_price, hotel_id FROM room_type')

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

# Gets all the cuisines, their info, and the restaurants with the cuisine from the database
@reservations.route('/Cuisine_Type', methods=['GET'])
def get_cuisines():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of cuisines
    cursor.execute('SELECT Cuisine_ID, Type, Description, Restaurant_ID, Name FROM Cuisine_Type '
                   + 'JOIN Restaurant_Cuisine ON Restaurant_Cuisine.Cuisine_ID = Cuisine_Type.Cuisine_ID'
                   + 'JOIN Restaurants ON Restaurants.Restaurant_ID = Restaurant_Cuisine.Restaurant_ID')

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