from sqlalchemy import Column, String, Date, Integer

from .db import Base


class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    host = Column(String)
    message = Column(String)
    date = Column(Date)

    def __init__(self, host, message, date):
        self.host = host
        self.message = message
        self.date = date