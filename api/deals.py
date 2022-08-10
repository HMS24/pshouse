from flask import Blueprint, abort

from api.models import Deal
from api.schemas import (
    DealRespSchema,
    ListedDealRespSchema,
    DealSchema,
)
from api.decorators import response, query_string

blueprint = Blueprint("deals", __name__)
listed_deal_resp_schema = ListedDealRespSchema()
deal_resp_schema = DealRespSchema()
deal_scema = DealSchema()


@blueprint.route("/deals", methods=["GET"])
@query_string(deal_scema)
@response(listed_deal_resp_schema)
def all(args):
    """Retrieve all deals"""
    return Deal.query.all()


@blueprint.route("/deals/<int:id>", methods=["GET"])
@response(deal_resp_schema)
def get(id):
    """Retrieve a deal by id"""
    return Deal.query.get(id) \
        or abort(404, f"Deal id {id} doesn't exist.")
