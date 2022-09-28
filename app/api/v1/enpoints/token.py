# Import standard library
from datetime import datetime, timedelta

import jwt
from app import app
# Import app code
from app.api.v1.enpoints.services import user_service
from app.core import config
from app.core.jwt import auth
from app.core.security import verify_password
from app.db.flask_session import db_session
# Import Schemas
from app.schemas.token import TokenSchema
# Import installed modules
from flask import abort
from webargs import fields


@app.post(f"{config.API_V1_STR}/login")
@app.input(
    {"email": fields.Str(required=True), "password": fields.Str(required=True)},
)
@app.output(TokenSchema)
@app.doc(
    summary="Login",
    description="OAuth2 compatible token login, get an access token for future requests",
    tags=["auth"],
)
def login(data):
    app.logger.info('email %s, password %s', data.get('email'), data.get('password'))
    user = user_service.find_by_email(data.get('email'), db_session)
    if not user or not verify_password(data.get('password'), user.password):
        abort(400, "Incorrect email or password")
    elif not user.is_active:
        abort(400, "Inactive user")
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({
        "sub": user.id,
        "email": user.email,
        "is_active": user.is_active,
        "exp": datetime.utcnow() + access_token_expires
    }, config.JWT_SECRET_KEY, algorithm="HS256")
    return {
        "access_token": token,
        "token_type": "Bearer",
    }
