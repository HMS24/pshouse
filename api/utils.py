from datetime import datetime, timedelta

DEFAULT_INTEVERAL_OF_DAYS = 30


def generate_inteveral_date_before(date, days=DEFAULT_INTEVERAL_OF_DAYS):
    start = datetime.timestamp(date - timedelta(days=days))
    end = datetime.timestamp(date)

    return (start, end)
