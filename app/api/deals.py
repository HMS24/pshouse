from flask import abort

from app.api import api
from app.models import Deal
from app.schemas import (
    DealRespSchema,
    ListedDealRespSchema,
    DealSchema,
)
from app.api.decorators import response, querystring

DEFAULT_OFFSET = 0
DEFAULT_LIMIT = 30

listed_deal_resp_schema = ListedDealRespSchema()
deal_resp_schema = DealRespSchema()
deal_scema = DealSchema()


@api.route("/deals", methods=["GET"])
@querystring(deal_scema)
@response(listed_deal_resp_schema)
def all(args):
    """Retrieve all deals"""
    city = args.get("city", None)
    district = args.get("district", None)
    from_ = args.get("from_date", None)
    to_ = args.get("to_date", None)
    sort_by = args.get("sort_by", "created_at")
    sort_rule = args.get("sort_rule", "asc")
    offset = args.get("offset", DEFAULT_OFFSET)
    limit = args.get("limit", DEFAULT_LIMIT)

    where_condition = (
        Deal.city == city,
        Deal.district == district,
        Deal.created_at.between(from_, to_)
    )

    sort_by = getattr(Deal, sort_by)
    order_condition = sort_by.desc() if sort_rule == "desc" else sort_by.asc()

    try:
        deals = (Deal
                 .query
                 .filter(*where_condition)
                 .order_by(order_condition)
                 .offset(offset)
                 .limit(limit)
                 .all())
    except Exception:
        abort(500)
    else:
        return deals


@api.route("/deals/<int:id>", methods=["GET"])
@response(deal_resp_schema)
def get(id):
    """Retrieve a deal by id"""
    return Deal.query.get(id) \
        or abort(404, f"Deal id {id} doesn't exist.")
