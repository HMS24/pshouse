import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from flask_migrate import Migrate, upgrade  # noqa
from app import create_app, db  # noqa

config = os.getenv("FLASK_CONFIG") or "docker"

app = create_app(config)
migrate = Migrate(app, db)


@app.cli.command()
def deploy():
    # migrate database to latest revision
    upgrade()
