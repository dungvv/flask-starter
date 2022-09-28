# Import standard library packages

# Import app code
from app import app
from app.api.v1 import api as api_v1  # noqa
from app.core import config
from app.db.flask_session import db_session
from app.db.init_db import init_db

# Set up CORS
from . import cors  # noqa
from . import errors  # noqa
from .jwt import jwt  # noqa

app.config["SECRET_KEY"] = config.SECRET_KEY


@app.teardown_appcontext
def shutdown_db_session(exception=None):
    db_session.remove()


@app.before_first_request
def setup():
    init_db(db_session)
