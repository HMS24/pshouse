from flask import Blueprint, jsonify

from api import db
from api.models import Deal

blueprint = Blueprint("deals", __name__)


@blueprint.route("/deals", methods=["GET"])
def all():
    """Retrieve all deals"""
    with db.Session() as session:
        deals = session.scalars(Deal.select()).all()

    return jsonify([d.to_dict() for d in deals])
