from flask import Flask, Blueprint

# create main blueprint
main_structure = Blueprint(__name__, "main_structure")


@main_structure.route("/")
def index():
    return "hello, world"


def create_app(config) -> Flask:
    """
    Factory for a Flask application.
    :param config: config object for the app
    :return: Flask app
    """
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(main_structure)

    return app
