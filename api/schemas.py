from datetime import datetime
from marshmallow import post_load
from api import ma
from api.models import Deal
from api.utils import generate_inteveral_date_before

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
    from_date = ma.DateTime()
    to_date = ma.DateTime()

    @post_load
    def set_default_query_date_if_not_exists(self, data, **kwargs):
        (default_from, default_to) = generate_inteveral_date_before(datetime.now())

        from_timestamp = data.get("from_timestamp", default_from)
        to_timestamp = data.get("to_timestamp", default_to)

        data["from_date"] = datetime.fromtimestamp(from_timestamp)
        data["to_date"] = datetime.fromtimestamp(to_timestamp)

        return data

class DealRespSchema(ma.Schema):
    data = ma.Nested(DealSchema)


class ListedDealRespSchema(ma.Schema):
    data = ma.List(ma.Nested(DealSchema))
