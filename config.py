import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    ALCHEMICAL_DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
