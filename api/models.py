import sqlalchemy as sqla

from api import db


class NewTaipeiCity(db.Model):
    __tablename__ = "new_taipei_city"

    id = sqla.Column(sqla.BigInteger, primary_key=True)

    # info
    district = sqla.Column(sqla.String(8), nullable=False, index=True)
    object_of_transaction = sqla.Column(sqla.String(16), nullable=False)
    location = sqla.Column(sqla.String(128), nullable=False)
    transaction_date = sqla.Column(sqla.DATE, nullable=False, index=True)
    level = sqla.Column(sqla.String(8), nullable=False)
    total_floor_numbers = sqla.Column(sqla.String(2), nullable=False)
    building_state = sqla.Column(sqla.String(16), nullable=False)
    main_use = sqla.Column(sqla.String(16), nullable=False)

    # area, room and buildings name
    land_total_area = sqla.Column(sqla.Float, nullable=False)
    building_total_area = sqla.Column(sqla.Float, nullable=False)
    room = sqla.Column(sqla.String(1), nullable=False)
    restaurant_and_living_room = sqla.Column(sqla.String(1), nullable=False)
    bathroom = sqla.Column(sqla.String(1), nullable=False)
    build_name = sqla.Column(sqla.String(32), nullable=False, index=True)
    buildings = sqla.Column(sqla.String(32), nullable=False)

    # car
    parking_sapce_type = sqla.Column(sqla.String(8), nullable=False)
    parking_sapce_total_area = sqla.Column(sqla.Float, nullable=False)
    parking_sapce_price = sqla.Column(sqla.Integer, nullable=False)

    # price
    price = sqla.Column(sqla.Integer, nullable=False)
    unit_price = sqla.Column(sqla.Integer, nullable=False)

    note = sqla.Column(sqla.String(128), nullable=False)

    created_at = sqla.Column(sqla.DateTime(timezone=True),
                             server_default=sqla.func.now())
    updated_at = sqla.Column(sqla.DateTime(timezone=True),
                             server_default=sqla.func.now(), onupdate=sqla.func.now())
