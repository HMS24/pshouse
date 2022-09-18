from flask import abort

from app.api import api
from app.models import Deal
from app.stores import get_deals_between_date
from app.schemas import (
    DealRespSchema,
    ListedDealRespSchema,
    DealSchema,
)
from app.api.decorators import response, querystring

listed_deal_resp_schema = ListedDealRespSchema()
deal_resp_schema = DealRespSchema()
deal_scema = DealSchema()

DEFAULT_CITY = "新北市"
DEFAULT_DISTRICT = "淡水區"
DEFAULT_OFFSET = 0
DEFAULT_LIMIT = 10


@api.route("/deals", methods=["GET"])
@querystring(deal_scema)
@response(listed_deal_resp_schema)
def all(args):
    """Retrieve all deals"""
    city = args.get("city", DEFAULT_CITY)
    district = args.get("district", DEFAULT_DISTRICT)
    from_ = args.get("from_")
    to_ = args.get("to_")
    search = args.get("search")
    sort = args.get("sort")
    start = args.get("start", DEFAULT_OFFSET)
    length = args.get("length", DEFAULT_LIMIT)

    # 轉成 [("colname", "desc")]
    orders = _transform_sort_by_order_pair_list(sort) if sort else []

    try:
        return get_deals_between_date(
            city=city,
            district=district,
            from_=from_,
            to_=to_,
            start=start,
            length=length,
            orders=orders,
            build_name=search,
        )
    except Exception as e:
        return abort(500, repr(e))


@api.route("/deals/<int:id>", methods=["GET"])
@response(deal_resp_schema)
def get(id):
    """Retrieve a deal by id"""
    return Deal.query.get(id) \
        or abort(404, f"Deal id {id} doesn't exist.")


def _transform_sort_by_order_pair_list(sort_str):
    can_sort_columns = [
        "price",
        "unit_price",
        "transaction_date",
    ]
    orders = []

    for s in sort_str.split(","):
        order = s[0]
        sort_by = s[1:]

        if sort_by not in can_sort_columns:
            sort_by = "transaction_date"

        order = "desc" if order == "-" else "asc"
        orders.append((sort_by, order))

    return orders
