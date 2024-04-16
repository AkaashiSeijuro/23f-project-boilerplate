from flask import Blueprint, request, jsonify, make_response
import json
from src import db


customers = Blueprint('customers', __name__)

# Get all customers from the DB
@customers.route('/customers', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select company, last_name,\
        first_name, job_title, business_phone from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get customer detail for customer with particular userID
@customers.route('/customers/<userID>', methods=['GET'])
def get_customer(userID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from customers where id = {0}'.format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# PUT route to update customer information
@customers.route('/customers/<int:userID>', methods=['PUT'])
def update_customer(userID):
    data = request.get_json()
    if data:
        cursor = db.get_db().cursor()
        cursor.execute('UPDATE customers SET Email=%s, Name=%s, Street=%s, City=%s, State=%s, ZipCode=%s WHERE id=%s',
                       (data.get('Email'), data.get('Name'), data.get('Street'),
                        data.get('City'), data.get('State'), data.get('ZipCode'), userID))
        db.get_db().commit()
        return jsonify({'message': 'Customer information updated successfully'}), 200
    else:
        return jsonify({'error': 'No data provided for update'}), 400