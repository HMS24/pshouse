from api import ma
from api.models import Deal


class DealSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Deal

    id = ma.auto_field()
    city = ma.String(required=True)
    district = ma.String(required=True)
    created_at = ma.DateTime()
    updated_at = ma.DateTime()


class DealRespSchema(ma.Schema):
    data = ma.Nested(DealSchema)


class ListedDealRespSchema(ma.Schema):
    data = ma.List(ma.Nested(DealSchema))
