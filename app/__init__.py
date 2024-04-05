from flask import Flask
import os

def create_app():
    # Create the Flask app
    app = Flask(__name__, static_folder='static')

    # Load configurations from environment variables
    app.config['FLASK_RUN_PORT'] = os.getenv('FLASK_RUN_PORT', 5000)

    # Register blueprints
    from .routes import auth, movie, tv, user, home
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)

    return app
