from app.models import Deal


def get_deals_between_date(
    city,
    district,
    from_,
    to_,
    build_name,
    orders,
    start,
    length,
):
    query = Deal.query

    # search filter
    filter_conditions = [
        Deal.city == city,
        Deal.district == district,
        Deal.transaction_date.between(from_, to_),
    ]

    if build_name:
        filter_conditions.append(Deal.build_name.like(f"%{build_name}%"))

    query = query.filter(*filter_conditions)
    total = query.count()

    # sorting
    order_conditions = [
        Deal.transaction_date.desc(),
    ]

    if orders:
        for sort_by, order in orders:
            field = getattr(Deal, sort_by)
            if order == "desc":
                sort_by = field.desc()
            order_conditions.append(field)

    query.order_by(*order_conditions)

    # pagination
    if start > -1 and length > -1:
        query = query.offset(start).limit(length)

    return {
        "data": query.all(),
        "total": total,
    }
