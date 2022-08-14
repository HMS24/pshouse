from datetime import datetime
from marshmallow import post_load

from app import ma
from app.models import Deal
from app.utils import generate_inteveral_date_before


class DealSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Deal

    id = ma.auto_field()
    city = ma.String(required=True)
    district = ma.String(required=True)
    created_at = ma.DateTime()
    updated_at = ma.DateTime()

    from_timestamp = ma.Integer()
    to_timestamp = ma.Integer()
    sort_by = ma.String()
    sort_rule = ma.String()
    page = ma.Integer()

    @post_load
    def set_default_query_date_if_not_exists(self, data, **kwargs):
        (default_from, default_to) = generate_inteveral_date_before(datetime.now())

        from_timestamp = data.get("from_timestamp", default_from)
        to_timestamp = data.get("to_timestamp", default_to)

        data["from_date"] = datetime.fromtimestamp(from_timestamp)
        data["to_date"] = datetime.fromtimestamp(to_timestamp)

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
