from datetime import datetime, timedelta

from app import config


def generate_start_end_timestamp(date, days=int(config.DATA_REVEAL_DAYS)):
    start = datetime.timestamp(date - timedelta(days=days))
    end = datetime.timestamp(date)

    return (start, end)
