from flask import url_for
from app.models import Deal

DEFAULT_DEALS_PER_PAGE = 2


def get_city_deals_between_date(
    city,
    district,
    from_date,
    to_date,
    page,
    sort_by="created_at",
    sort_rule="desc",
    page_error_out=False,
    page_endpoint=None,
):
    where_condition = (
        Deal.city == city,
        Deal.district == district,
        Deal.created_at.between(from_date, to_date),
    )

    _sort_by = getattr(Deal, sort_by)
    order_condition = _sort_by.desc() if sort_rule == "desc" else _sort_by.asc()

    page_condition = {
        "page": page,
        "per_page": DEFAULT_DEALS_PER_PAGE,
        "error_out": page_error_out,
    }

    pagination = (
        Deal.query
        .filter(*where_condition)
        .order_by(order_condition)
        .paginate(**page_condition)
    )

    _args = {
        "city": city,
        "district": district,
        "from_timestamp": int(from_date.timestamp()),
        "to_timestamp": int(to_date.timestamp()),
        "sort_by": sort_by,
        "sort_rule": sort_rule,
    }

    prev = url_for(page_endpoint, **_args, page=page-1) if pagination.has_prev else None
    next = url_for(page_endpoint, **_args, page=page+1) if pagination.has_next else None

    return {
        "data": pagination.items,
        "total": pagination.total,
        "prev": prev,
        "next": next,
    }
