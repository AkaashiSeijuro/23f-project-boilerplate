from flask import Blueprint, request, jsonify, make_response
import json
from src import db

reservations = Blueprint('reservations', __name__)

# Routes for Reservations
@reservations.route('/reservations', methods=['GET'])
def get_reservations():
    # Logic to retrieve all reservations
    return jsonify(reservations)

@reservations.route('/reservations/<reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    # Logic to retrieve a specific reservation
    return jsonify(reservations)

@reservations.route('/reservations', methods=['POST'])
def create_reservation():
    # Logic to create a new reservation
    data = request.get_json()
    # Process data and create reservation
    return jsonify(new_reservation), 201

@reservations.route('/reservations/<reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    # Logic to update an existing reservation
    data = request.get_json()
    # Process data and update reservation
    return jsonify(updated_reservation)

@reservations.route('/reservations/<reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    # Logic to delete a reservation
    # Delete reservation with ID reservation_id
    return jsonify({'message': 'Reservation deleted'}), 204  # 204 for successful deletion

# Routes for Hotel
@reservations.route('/hotels', methods=['GET'])
def get_hotels():
    # Logic to retrieve all hotels
    return jsonify(hotels)