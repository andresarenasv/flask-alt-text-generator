import cv2
import numpy as np
from werkzeug.datastructures import FileStorage
from flask import send_file
import io

def process_image_to_grayscale(file: FileStorage):
    """Process image file to grayscale and return as downloadable response"""
    # Read image file
    filestr = file.read()
    npimg = np.frombuffer(filestr, np.uint8)
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Convert back to bytes
    _, img_encoded = cv2.imencode('.jpg', gray_image)
    
    # Prepare the response
    return send_file(
        io.BytesIO(img_encoded.tobytes()),
        mimetype='image/jpeg',
        as_attachment=True,
        download_name='grayscale.jpg'
    ) 