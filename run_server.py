"""Script to run the server."""
from rsa.cryptography.app import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(port=2345)
