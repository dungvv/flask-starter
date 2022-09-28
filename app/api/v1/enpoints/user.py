from webargs import fields

from app import app
from app.api.v1.enpoints.services import user_service
from app.core import config
from app.db.flask_session import db_session
from app.schemas import TokenSchema


@app.post(f"{config.API_V1_STR}/register")
@app.input(
    {
        "email": fields.Str(required=True),
        "password": fields.Str(required=True),
        "first_name": fields.Str(),
        "last_name": fields.Str(),
    }
)
@app.output(TokenSchema)
@app.doc(summary="Register user", description="Register new user", tags=["users"])
def register_user(data):
    return user_service.register_user(data, db_session)
