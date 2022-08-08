from flask import Blueprint, jsonify
from api.models import Deal

blueprint = Blueprint("deals", __name__)


@blueprint.route("/deals", methods=["GET"])
def all():
    """Retrieve all deals"""
    results = [d.to_dict() for d in Deal.query.all()]

    return jsonify(results)
