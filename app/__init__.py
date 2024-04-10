from flask import Flask
import os
import logging
import sys


def create_app():
    # Create the Flask app
    app = Flask(__name__, static_folder="static")

    # Load configurations from environment variables
    app.config["FLASK_RUN_PORT"] = os.getenv("FLASK_RUN_PORT", 5000)
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.DEBUG)

    # Register blueprints
    from .routes import auth, movie, tv, user, home

    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(movie.bp)
    app.register_blueprint(tv.bp)

    return app
