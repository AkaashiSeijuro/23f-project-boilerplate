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


@transportation.route('/flight_ticket', methods=['GET'])
def get_ticket_detail():
    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    # Execute database query to retrieve all ticket information
    cursor.execute('SELECT * FROM flight_ticket')

    # Fetch the column headers from the cursor description
    row_headers = [x[0] for x in cursor.description]

    # Fetch all the data from the cursor
    the_data = cursor.fetchall()

    # Create a list of dictionaries containing ticket information
    json_data = [dict(zip(row_headers, row)) for row in the_data]

    # Return JSON response with ticket information and status code 200 (OK)
    return jsonify(json_data), 200

# Update the class of the ticket with this TicketID
@transportation.route('/flight_ticket/<TicketID>', methods=['PUT'])
def update_ticket_class(TicketID):
    cust_data = request.get_json()

    cursor = db.get_db().cursor()
    cursor.execute('UPDATE flight_ticket SET Class=%s WHERE TicketID=%s',
                   (cust_data.get('Class'), TicketID))
    db.get_db().commit()

    return jsonify({'message': 'Ticket class updated successfully'})

# Delete the ticket with this TicketID
@transportation.route('/flight_ticket/<TicketID>', methods=['DELETE'])
def delete_ticket(TicketID):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM flight_ticket WHERE TicketID=%s', (TicketID))
    db.get_db().commit()

    return jsonify({'message': 'Ticket deleted successfully'})

# Create a new ticket
@transportation.route('/flight_ticket', methods=['POST'])
def add_new_ticket():
    try:
        # Check if request contains JSON data
        if not request.json:
            return jsonify({'error': 'No JSON data received'}), 400

        # Extract data from JSON request
        ticket_data = request.json
        id = ticket_data.get('TicketID')
        seat_class = ticket_data.get('Class')
        customer_name = ticket_data.get('customerName')
        cost = ticket_data.get('cost')
        customer_id = ticket_data.get('CustomerID')
        flight_no = ticket_data.get('flight_no')

        # Validate required fields
        if not all([id, seat_class, customer_name, cost, customer_id, flight_no]):
            return jsonify({'error': 'Missing required fields'}), 400

        # Construct and execute SQL query
        query = f'INSERT INTO flight_ticket (TicketID, Class, customerName, cost, CustomerID, flight_no) VALUES ({id}, "{seat_class}", "{customer_name}", {cost}, {customer_id}, {flight_no})'
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        return jsonify({'success': True, 'message': 'Ticket added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Gets all navigation routes and their info from the database
@transportation.route('/Navigation', methods=['GET'])
def get_navigation_routes():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of navigation routes
    cursor.execute('SELECT Navigation_ID, Routing, Estimated_time, Fare, Distance, Transportation_Method FROM Navigation')

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
        # Convert estimated_time to a string before adding it to the dictionary
        row_dict = dict(zip(column_headers, row))
        row_dict['Estimated_time'] = str(row_dict['Estimated_time'])
        json_data.append(row_dict)

    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

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