from .utils.processors import process_image_to_grayscale
from werkzeug.datastructures import FileStorage
from flask import send_file

class ImageService:
    def to_grayscale(self, file: FileStorage):
        """Convert image to grayscale"""
        processed_image = process_image_to_grayscale(file)
        return processed_image 