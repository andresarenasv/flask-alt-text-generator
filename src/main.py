from flask import Flask
from src.modules.number.routes import number_bp
from src.modules.image.routes import image_bp
from src.modules.replicate.routes import replicate_bp

def create_app():
    app = Flask(__name__)
        
    # Register blueprints
    app.register_blueprint(number_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(replicate_bp)

    return app

if __name__ == '__main__':
    app = create_app()