from flask import (
    abort,
    current_app,
    url_for,
)

from app.api import api
from app.models import Deal
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
    DEFAULT_DEALS_PAGE = current_app.config["DEFAULT_DEALS_PAGE"]
    DEFAULT_DEALS_PER_PAGE = current_app.config["DEFAULT_DEALS_PER_PAGE"]

    city = args.get("city", None)
    district = args.get("district", None)
    from_ = args.get("from_date", None)
    to_ = args.get("to_date", None)
    sort_by = args.get("sort_by", "created_at")
    sort_rule = args.get("sort_rule", "desc")
    page = args.get("page", DEFAULT_DEALS_PAGE)

    where_condition = (
        Deal.city == city,
        Deal.district == district,
        Deal.created_at.between(from_, to_),
    )

    _sort_by = getattr(Deal, sort_by)
    order_condition = _sort_by.desc() if sort_rule == "desc" else _sort_by.asc()

    page_condition = {
        "page": page,
        "per_page": DEFAULT_DEALS_PER_PAGE,
        "error_out": False,
    }

    try:
        pagination = (
            Deal.query
                .filter(*where_condition)
                .order_by(order_condition)
                .paginate(**page_condition)
        )

        _args = {
            "city": city,
            "district": district,
            "from_date": from_,
            "to_date": to_,
            "sort_by": sort_by,
            "sort_rule": sort_rule,
        }

        prev = url_for("api.all", **_args, page=page-1) if pagination.has_prev else None
        next = url_for("api.all", **_args, page=page+1) if pagination.has_next else None

    except Exception as e:
        abort(500, repr(e))
    else:
        return {
            "data": pagination.items,
            "count": len(pagination.items),
            "total": pagination.total,
            "prev": prev,
            "next": next,
        }


@api.route("/deals/<int:id>", methods=["GET"])
@response(deal_resp_schema)
def get(id):
    """Retrieve a deal by id"""
    return Deal.query.get(id) \
        or abort(404, f"Deal id {id} doesn't exist.")
