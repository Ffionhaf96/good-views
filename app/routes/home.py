from flask import Blueprint, jsonify


bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'Home'})