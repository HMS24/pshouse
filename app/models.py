import sqlalchemy as sa

from app import db


class Deal(db.Model):
    __tablename__ = "deals"

    id = sa.Column(sa.BigInteger, primary_key=True)

    # info
    city = sa.Column(sa.String(3), nullable=False, index=True)
    district = sa.Column(sa.String(8), nullable=False, index=True)
    object_of_transaction = sa.Column(sa.String(16), nullable=False)
    location = sa.Column(sa.String(128), nullable=False)
    transaction_date = sa.Column(sa.DATE, nullable=False, index=True)
    level = sa.Column(sa.String(8), nullable=False)
    total_floor_numbers = sa.Column(sa.String(2), nullable=False)
    building_state = sa.Column(sa.String(16), nullable=False)
    main_use = sa.Column(sa.String(16), nullable=False)

    # area, room and buildings name
    land_total_area = sa.Column(sa.Float, nullable=False)
    building_total_area = sa.Column(sa.Float, nullable=False)
    room = sa.Column(sa.String(1), nullable=False)
    restaurant_and_living_room = sa.Column(sa.String(1), nullable=False)
    bathroom = sa.Column(sa.String(1), nullable=False)
    build_name = sa.Column(sa.String(32), nullable=False, index=True)
    buildings = sa.Column(sa.String(32), nullable=False)

    # car
    parking_sapce_type = sa.Column(sa.String(8), nullable=False)
    parking_sapce_total_area = sa.Column(sa.Float, nullable=False)
    parking_sapce_price = sa.Column(sa.Integer, nullable=False)

    # price
    price = sa.Column(sa.Integer, nullable=False)
    unit_price = sa.Column(sa.Integer, nullable=False)

    note = sa.Column(sa.String(128), nullable=False)

    created_at = sa.Column(sa.DateTime(timezone=True),
                           server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime(timezone=True),
                           server_default=sa.func.now(), onupdate=sa.func.now())


class DealStatistics(db.Model):

    __tablename__ = "deal_statistics"
    __table_args__ = (
        db.UniqueConstraint(
            "city",
            "district",
            "year",
            "month",
            "build_name",
            "room",
            name="uc_city_district_year_month_buildname_room",
        ),
    )

    id = sa.Column(
        sa.Integer,
        primary_key=True,
    )
    city = sa.Column(
        sa.String(3),
        nullable=False,
    )
    district = sa.Column(
        sa.String(8),
        nullable=False,
    )
    year = sa.Column(
        sa.String(4),
        nullable=False,
    )
    month = sa.Column(
        sa.String(2),
        nullable=False,
    )
    build_name = sa.Column(
        sa.String(32),
        nullable=False,
    )
    room = sa.Column(
        sa.String(1),
        nullable=False,
    )
    count_num = sa.Column(
        sa.Integer,
        nullable=False,
    )
    avg_total_price = sa.Column(
        sa.Integer,
        nullable=False,
    )
    avg_house_price = sa.Column(
        sa.Integer,
        nullable=False,
    )
    avg_house_unit_price = sa.Column(
        sa.Integer,
        nullable=False,
    )
    created_at = sa.Column(
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
    )
    updated_at = sa.Column(
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        onupdate=sa.func.now(),
    )
