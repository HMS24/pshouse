from datetime import datetime
from marshmallow import post_load

from app import ma
from app.models import Deal
from app.utils import generate_inteveral_date_before


class DealSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Deal

    # request
    from_ = ma.Integer()    # timestamp
    to_ = ma.Integer()  # timestamp
    search = ma.String()
    sort = ma.String()
    start = ma.Integer()
    length = ma.Integer()

    # response
    id = ma.auto_field()
    city = ma.String()
    district = ma.String()
    object_of_transaction = ma.String()
    location = ma.String()
    transaction_date = ma.Date()
    building_total_area = ma.Float()
    parking_sapce_total_area = ma.Float()
    room = ma.Integer()
    restaurant_and_living_room = ma.Integer()
    bathroom = ma.Integer()
    build_name = ma.String()
    buildings = ma.String()
    level = ma.String()
    price = ma.Integer()
    unit_price = ma.Integer()
    parking_sapce_price = ma.Integer()
    parking_sapce_type = ma.String()
    note = ma.String()
    created_at = ma.DateTime()
    updated_at = ma.DateTime()

    @post_load
    def set_default_query_date_if_not_exists(self, data, **kwargs):
        (default_from, default_to) = generate_inteveral_date_before(datetime.now())

        from_ = data.get("from_", default_from)
        to_ = data.get("to_", default_to)

        # timestamp to datetime
        data["from_"] = datetime.fromtimestamp(from_)
        data["to_"] = datetime.fromtimestamp(to_)

        return data


class DealRespSchema(ma.Schema):
    result = ma.Nested(DealSchema)


class PageSchema(ma.Schema):
    data = ma.List(ma.Nested(DealSchema))
    prev = ma.String(dump_only=True)
    next = ma.String(dump_only=True)
    count = ma.Integer(dump_only=True)
    total = ma.Integer(dump_only=True)


class ListedDealRespSchema(ma.Schema):
    result = ma.Nested(PageSchema)
