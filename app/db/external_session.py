from app.core import config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

repeatable_read_engine = engine.execution_options(isolation_level='SERIALIZABLE')
