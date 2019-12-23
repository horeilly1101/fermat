"""File that contains the create_app factory function."""
from flask import Flask, Blueprint

# create main blueprint
main_structure = Blueprint(__name__, "main_structure")


@main_structure.route("/get-key/")
def index():
    return "Hello, world!"


def create_app(config) -> Flask:
    """
    Factory for a Flask application.
    :param config: config object for the app
    :return: Flask app
    """
    app = Flask(__name__)
    app.config.from_object(config)

    # register blueprints
    app.register_blueprint(main_structure)

    # configure extensions ...

    return app
