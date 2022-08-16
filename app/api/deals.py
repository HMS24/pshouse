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


@api.route("/deals", methods=["GET"])
@querystring(deal_scema)
@response(listed_deal_resp_schema)
def all(args):
    """Retrieve all deals"""
    city = args.get("city", "新北市")
    district = args.get("district", "淡水區")
    from_ = args.get("from_")
    to_ = args.get("to_")
    search = args.get("search")
    sort = args.get("sort")
    start = args.get("start", -1)
    length = args.get("length", -1)

    # 轉成 [("colname", "desc")]
    orders = []
    if sort:
        for s in sort.split(","):
            order = s[0]
            sort_by = s[1:]

            if sort_by not in ["price", "unit_price", "parking_sapce_price"]:
                sort_by = "price"

            order = "desc" if order == "-" else "asc"
            orders.append((sort_by, order))

    try:
        return get_deals_between_date(
            city=city,
            district=district,
            from_=from_,
            to_=to_,
            build_name=search,
            orders=orders,
            start=start,
            length=length,
        )
    except Exception as e:
        return abort(500, repr(e))


@api.route("/deals/<int:id>", methods=["GET"])
@response(deal_resp_schema)
def get(id):
    """Retrieve a deal by id"""
    return Deal.query.get(id) \
        or abort(404, f"Deal id {id} doesn't exist.")
