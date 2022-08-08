import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)10.19s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
)

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_cls=Config):
    app = Flask(__name__)
    app.config.from_object(config_cls)

    from api import models
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprints
    from api.errors import blueprint as error_bp
    app.register_blueprint(error_bp)

    @app.route("/")
    def index():
        return "<p>Hello, World!</p>"

    return app
