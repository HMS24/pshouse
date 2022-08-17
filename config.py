import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "app-dev.db")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("PROD_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "app-prod.db")


class DockerConfig(ProductionConfig):

    @staticmethod
    def init_app(app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler

        formatter = logging.Formatter("%(asctime)10.19s [%(levelname)s] %(message)s")
        handler = StreamHandler()
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)

        app.logger.addHandler(handler)


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "docker": DockerConfig,
}
