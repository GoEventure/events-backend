from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.core.db.session import Base


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

    class Config:
        orm_mode = True
