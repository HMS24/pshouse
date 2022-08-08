import logging

from flask import Flask

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)10.19s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
)


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<p>Hello, World!</p>"

    return app
