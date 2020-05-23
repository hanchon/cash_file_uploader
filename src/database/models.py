from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Caso(Base):
    __tablename__ = 'caso'
    id = Column(Integer, primary_key=True)
    generated_id = Column(String)
    tx_hash = Column(String)
    created = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"Caso: {self.generated_id}"
