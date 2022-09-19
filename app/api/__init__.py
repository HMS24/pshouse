from flask import Blueprint

api = Blueprint("api", __name__)

from app.api import deals  # noqa
from app.api import deal_statistics  # noqa
