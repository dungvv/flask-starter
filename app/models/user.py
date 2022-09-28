from datetime import datetime

from sqlalchemy import Column, String, Boolean, DateTime, BigInteger

from app.models.base_class import CustomBase, BaseInfo


class User(CustomBase):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    created_by = Column(BigInteger)
    updated_by = Column(BigInteger)


