"""Script to run the server."""
from rsa.app import create_app
from rsa.config import Config


if __name__ == "__main__":
    app = create_app(Config)
    app.run(port=2345)
