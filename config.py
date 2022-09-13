import os

basedir = os.path.abspath(os.path.dirname(__file__))

DAY_OF_A_YEAR = 365


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = False
    DATA_REVEAL_DAYS = os.getenv("DATA_REVEAL_DAYS") or DAY_OF_A_YEAR

    @staticmethod
    def init_app(app):
        pass


class DockerConfig(Config):

    @staticmethod
    def init_app(app):
        Config.init_app(app)


class TestConfig(Config):
    DEBUG = False
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI") or "sqlite:///:memory:"


config = {
    "docker": DockerConfig,
    "test": TestConfig,
}
