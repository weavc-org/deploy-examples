from dataclasses import dataclass
from sqlalchemy import Column, String, DateTime, Integer, desc
from datetime import datetime
from core.database.db import DBBase, session_factory

@dataclass
class Log(DBBase):
    id: int
    host: str
    message: str
    date: datetime

    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    host = Column(String)
    message = Column(String)
    date = Column(DateTime(timezone=True))

def create_log(host: str, message: str):
    # create session
    session = session_factory()
    # create log
    m = Log(host=host, message=message, date=datetime.now())
    # add and commit log
    session.add(m)
    session.commit()
    # close connection and return the id of the new log
    id = m.id
    session.close()
    return id

def get_logs(count: int = None, page: int = None):
    session = session_factory()
    log_query = session.query(Log).order_by(desc(Log.date))
    session.close()

    if (count is not None):
        log_query = log_query.limit(count)
        # page requires a count to be provided
        if (page is not None):
            log_query = log_query.offset(count*(page-1))

    return log_query.all()