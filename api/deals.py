from flask import (
    Blueprint,
    abort,
)

from api.models import Deal
from api.schemas import (
    DealRespSchema,
    ListedDealRespSchema,
)
from api.decorators import response

blueprint = Blueprint("deals", __name__)
listed_deal_resp_schema = ListedDealRespSchema()
deal_resp_schema = DealRespSchema()


@blueprint.route("/deals", methods=["GET"])
@response(listed_deal_resp_schema)
def all():
    """Retrieve all deals"""
    return Deal.query.all()


@blueprint.route("/deals/<int:id>", methods=["GET"])
@response(deal_resp_schema)
def get(id):
    """Retrieve a deal by id"""
    return Deal.query.get(id) \
        or abort(404, f"Deal id {id} doesn't exist.")
