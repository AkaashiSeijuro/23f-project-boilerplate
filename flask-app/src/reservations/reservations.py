from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

reservations = Blueprint('reservations', __name__)

# Add a new customer to the hotel
@reservations.route('/hotel', methods=['POST'])
def add_customer_to_hotel():
    # collecting data from the request object
    cust_data = request.get_json()
    current_app.logger.info(cust_data)

    # extracting the variable
    customerID = cust_data['CustomerID']
    email = cust_data['Email']
    name = cust_data['Name']
    street = cust_data['Street']
    city = cust_data['City']
    state = cust_data['State']
    zipcode = cust_data['ZipCode']
    restaurantID = cust_data['Restaurant_ID']
    hotelID = cust_data['Hotel_id']

    # constructing the query
    query = 'insert into hotel (CustomerID, Email, Name, Street, City, State, ZipCode, Restaurant_ID, Hotel_id) values ("'
    query += str(customerID) + '", "'
    query += email + '", "'
    query += name + '", "'
    query += street + '", "'
    query += city + '", "'
    query += state + '", "'
    query += str(zipcode) + '", "'
    query += str(restaurantID) + '", "'
    query += str(hotelID) + '")'
    current_app.logger.info(query)

    # executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Success!'

# Delete a customer from the hotel with this Hotel

# Get all the hotels and their info from the database
@reservations.route('/hotel', methods=['GET'])
def get_hotels(): 
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of hotels
    cursor.execute('SELECT hotel_id, amentities, street, city, state, zipcode, duration, rating FROM hotel')

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
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

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
def update_reservation_time(Booked_ID):
    cust_data = request.get_json()

    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Restaurants_Booked SET Datetime=%s WHERE Booked_ID=%s',
                     (cust_data.get('Datetime'), Booked_ID))
    db.get_db().commit()

    return jsonify({'message': 'Restaurant reservation time updated successfully'})

# Deletes the reservation at the restaurant with the given Reservation_ID
@reservations.route('/Restaurants_Booked/<Booked_ID>', methods=['DELETE'])
def delete_reservation(Booked_ID):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Restaurants_Booked WHERE Booked_ID=%s', (Booked_ID,))
    db.get_db().commit()

    return jsonify({'message': 'Restaurant reservation deleted successfully'})

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
                   + 'JOIN Restaurants ON Restaurants.restaurant_Id = Restaurant_Cuisine.restaurant_Id')

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