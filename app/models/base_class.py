from datetime import datetime

from snowflake import SnowflakeGenerator
from sqlalchemy import Column, BigInteger, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base, declared_attr

gen = SnowflakeGenerator(2)


def next_snowflake_id():
    return next(gen)


Base = declarative_base()


class CustomBase(Base):
    __abstract__ = True

    id: int = Column(BigInteger, primary_key=True, index=True, autoincrement=False)

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(**kwargs)
        if self.id is None:
            self.id = next_snowflake_id()
        self.__dict__.update(**kwargs)


class BaseInfo:
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    created_by = Column(BigInteger)
    updated_by = Column(BigInteger)
    is_deleted = Column(Boolean, default=False)


class CustomBaseSnowIdSecondary(CustomBase, BaseInfo):
    __abstract__ = True


class CustomBaseSecondary(Base, BaseInfo):
    __abstract__ = True