from app.api import api
from app.api.decorators import response
from app.schemas import ListedDealStatisticsSchema
from app.stores import get_deal_statistics

listed_deal_statistics_schema = ListedDealStatisticsSchema()


@api.route("/deal-statistics", methods=["GET"])
@response(listed_deal_statistics_schema)
def get_deal_statistics_():
    """Retrieve all deal statistics"""
    return get_deal_statistics()
