# Import standard library modules

# Import installed modules
# Import app code
import jwt
from apiflask import HTTPTokenAuth, abort
from app import app
from app.core import config
from app.db.flask_session import db_session

# Set up the Flask-JWT-Extended extension
from app.models.user import User

app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY

auth = HTTPTokenAuth(scheme='Bearer')


class CurrentUser:
    id: int
    email: str
    is_active: bool

    def __init__(self, id, email, is_active):
        self.id = id
        self.email = email
        self.is_active = is_active


@auth.verify_token
def verify_token(token):
    if token == '':
        return abort(401, "Unauthenticated")
    decoded = jwt.decode(token, config.JWT_SECRET_KEY, algorithms="HS256")
    user_id = decoded['sub']
    user = db_session.query(User).filter(User.id == user_id).first()
    return CurrentUser(id=user.id, shop_id=None, email=user.email, is_active=user.is_active)


# @auth.get_user_roles
# def get_user_roles(user):
#     return user.roles
