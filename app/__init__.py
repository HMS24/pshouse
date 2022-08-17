from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config as config_dict

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):
    app = Flask(__name__)

    config = config_dict[config_name]
    app.config.from_object(config)

    config.init_app(app)
    db.init_app(app)
    ma.init_app(app)

    # blueprints
    from app.errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/apiv1")

    return app
