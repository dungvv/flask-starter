from app.db.external_session import engine
from app.models.base_class import Base


def init_db(db_session):
    Base.metadata.create_all(bind=engine)
