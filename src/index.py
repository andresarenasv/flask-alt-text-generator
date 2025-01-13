from flask import Flask, request
from src.modules.number.routes import number_bp
from src.modules.image.routes import image_bp
from src.modules.replicate.routes import replicate_bp


app = Flask(__name__)

# Register blueprints
app.register_blueprint(number_bp)
app.register_blueprint(image_bp)
app.register_blueprint(replicate_bp)

@app.route("/")
def index():
    return "This is an alt tag generator!"

@app.route('/health')
def health_check():
    return {'status': 'ok'}