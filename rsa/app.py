"""File that contains the create_app factory function."""
from flask import Flask, Blueprint
import json
from rsa.rsa import RSAAlgorithm

# create main blueprint
main_structure = Blueprint(__name__, "main_structure")


@main_structure.route("/get-key/<min_bits>")
def get_key(min_bits):
    algo = RSAAlgorithm(int(min_bits), int(min_bits) + 8)
    return json.dumps({
        "publicKey": hex(algo.public_key),
        "privateKey": hex(algo.private_key),
        "modulus": hex(algo.modulus)
    })


def create_app() -> Flask:
    """
    Factory for a Flask application.
    :return: Flask app
    """
    app = Flask(__name__)

    # register blueprints
    app.register_blueprint(main_structure)

    # configure extensions ...

    return app
