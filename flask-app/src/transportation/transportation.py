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
@transportation.route('/flight_ticket/<TicketID>', methods=['GET'])
def get_ticket_detail (flight_no):

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

# Create a new ticket
@transportation.route('/flight_ticket', methods=['POST'])
def add_new_ticket():
    
    # collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # extracting the variable 
    id = the_data['TicketID']
    seatClass = the_data['Class']
    customerName = the_data['customerName']
    cost = the_data['cost']
    customerID = the_data['CustomerID']
    flight_no = the_data['flight_no']

    # constructing the query
    query = 'insert into flight_ticket (TicketID, Class, customerName, cost, CustomerID, flight_no) values ("'
    query += str(id) + '", "'
    query += seatClass + '", "'
    query += customerName + '", "'
    query += str(cost) + '", "'
    query += str(customerID) + '", "'
    query += str(flight_no) + '")'
    current_app.logger.info(query)

    # executing and comitting the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Gets all navigation routes and their info from the database
@transportation.route('/Navigation', methods=['GET'])
def get_navigation_routes():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of navigation routes
    cursor.execute('SELECT Navigation_ID, Routing, Estimated_time, Fare, Distance, Transportation_Method FROM navigation')

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

# Gets all payments and their info from the database
def get_payment_info():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of payments
    cursor.execute('SELECT paymentID, payment_type, amount, transaction_assured, theft_protection, TicketID FROM payments')

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