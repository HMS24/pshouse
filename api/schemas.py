from api import ma
from api.models import Deal


class DealSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Deal

    id = ma.auto_field()
    city = ma.String()
    district = ma.String()
    created_at = ma.DateTime()
    updated_at = ma.DateTime()


class NestedDealSchema(ma.SQLAlchemySchema):
    data = ma.List(ma.Nested(DealSchema))
