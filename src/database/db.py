from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from database.models import Base
from config import SQLALCHEMY_DATABASE_URI, POOL_SIZE, MAX_OVERFLOW

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=POOL_SIZE, max_overflow=MAX_OVERFLOW)


def create_models():
    Base.metadata.create_all(engine)


def create_session():
    return scoped_session(sessionmaker(bind=engine))