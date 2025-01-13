from flask import Blueprint, jsonify
from src.modules.number.service import NumberService

number_bp = Blueprint('number', __name__, url_prefix='/number')
number_service = NumberService()

@number_bp.route('/random', methods=['GET'])
def get_random_number():
    """Get a random number between 1 and 100"""
    try:
        result = number_service.generate_random_number()
        return jsonify({'number': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500 