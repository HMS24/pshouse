import json
from datetime import datetime

from tests.base import BaseTestCase
from app import db
from app.models import Deal

with open("tests/mock/deals.json", "r", encoding="utf-8") as f:
    result = json.load(f)["result"]
    expected_deals = result["data"]
    expected_total = result["total"]


class DealTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        for item in expected_deals:
            deal = Deal(**item)

            for col in ["created_at", "updated_at", "transaction_date"]:
                value = getattr(deal, col)
                try:
                    setattr(deal, col, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S"))
                except ValueError:
                    setattr(deal, col, datetime.strptime(value, "%Y-%m-%d"))

            db.session.add(deal)
        db.session.commit()

    def test_get_deals_without_querystring(self):
        resp = self.client.get("/apiv1/deals")
        result = json.loads(resp.get_data(as_text=True))["result"]

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(result["data"]), expected_total)
        self.assertListEqual(result["data"], expected_deals)
