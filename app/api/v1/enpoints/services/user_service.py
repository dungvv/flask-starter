from datetime import timedelta, datetime

import jwt
from apiflask import abort

from app.core import config
from app.core.security import get_password_hash
from app.models.user import User
from app.schemas import TokenSchema


def find_by_email(email: str, db_session) -> User:
    return db_session.query(User).filter(User.email == email).first()


def register_user(data, db_session) -> TokenSchema:
    user_old = find_by_email(data.get('email'), db_session)
    if user_old:
        abort(400, f"The user with this email already exists in the system: {data.get('email')}")
    user = User(
        email=data.get('email'),
        password=get_password_hash(data.get('password')),
        first_name=data.get('first_name'),
        last_name=data.get('last_name')
    )
    db_session.add(user)
    db_session.commit()
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({
        "sub": user.id,
        "email": user.email,
        "is_active": user.is_active,
        "exp": datetime.utcnow() + access_token_expires
    }, config.JWT_SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "Bearer"}
