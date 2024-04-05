from flask import Blueprint, request, jsonify
from controllers.user import create_user
# Create a Blueprint for the auth routes
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "GET":
        return 'Hello'
    # Get data from request
    data = request.form
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if create_user(username=username, password=password, email=email):
        return jsonify({'message': 'User created successfully'}), 201
    
    return jsonify({'message': 'Failed to create user'}), 400


@bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status': False})