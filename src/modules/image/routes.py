from flask import Blueprint, request, jsonify
from src.modules.image.service import ImageService

image_bp = Blueprint('image', __name__, url_prefix='/image')
image_service = ImageService()

@image_bp.route('/process', methods=['POST'])
def process_image():
    """Convert an image to grayscale"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
            
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
            
        if not file or not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return jsonify({'error': 'Invalid file format'}), 400

        return image_service.to_grayscale(file)

    except Exception as e:
        return jsonify({'error': str(e)}), 500 