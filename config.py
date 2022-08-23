import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = False

    @staticmethod
    def init_app(app):
        pass


class DockerConfig(Config):

    @staticmethod
    def init_app(app):
        Config.init_app(app)


config = {
    "docker": DockerConfig,
}
