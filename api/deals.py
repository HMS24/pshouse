from flask import Blueprint

from api import db
from api.models import Deal
from api.schemas import NestedDealSchema

blueprint = Blueprint("deals", __name__)
nested_deals_schema = NestedDealSchema()


@blueprint.route("/deals", methods=["GET"])
def all():
    """Retrieve all deals"""
    with db.Session() as session:
        deals = session.scalars(Deal.select()).all()

    return nested_deals_schema.jsonify({"data": deals})
