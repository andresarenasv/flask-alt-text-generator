from flask import Blueprint, jsonify, request
from src.modules.replicate.service import ReplicateService

replicate_bp = Blueprint('replicate', __name__, url_prefix='/replicate')
replicate_service = ReplicateService()

@replicate_bp.route('/alt-text', methods=['GET'])
def get_alt_text():
    # Get imageUrl query param
    args = request.args
    imageUrl = args.to_dict().get('imageUrl')
    try:
        result = replicate_service.generate_alt_text(imageUrl)
        return jsonify({'altText': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500 