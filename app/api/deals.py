from flask import abort

from app.api import api
from app.models import Deal
from app.stores import get_city_deals_between_date
from app.schemas import (
    DealRespSchema,
    ListedDealRespSchema,
    DealSchema,
)
from app.api.decorators import response, querystring

listed_deal_resp_schema = ListedDealRespSchema()
deal_resp_schema = DealRespSchema()
deal_scema = DealSchema()


@api.route("/deals", methods=["GET"])
@querystring(deal_scema)
@response(listed_deal_resp_schema)
def all(args):
    """Retrieve all deals"""
    city = args.get("city")
    district = args.get("district")
    from_date = args.get("from_date")
    to_date = args.get("to_date")
    page = args.get("page", 1)

    try:
        return get_city_deals_between_date(
            city=city,
            district=district,
            from_date=from_date,
            to_date=to_date,
            page=page,
            page_endpoint="api.all",
        )
    except Exception as e:
        return abort(500, repr(e))


@api.route("/deals/<int:id>", methods=["GET"])
@response(deal_resp_schema)
def get(id):
    """Retrieve a deal by id"""
    return Deal.query.get(id) \
        or abort(404, f"Deal id {id} doesn't exist.")
