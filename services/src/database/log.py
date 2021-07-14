from sqlalchemy import Column, String, Date, Integer
from datetime import date, datetime

from .db import DBBase, session_factory

class Log(DBBase):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    host = Column(String)
    message = Column(String)
    date = Column(Date)

    def __init__(self, host, message, date):
        self.host = host
        self.message = message
        self.date = date

    def __repr__(self):
       return "<Log(id='%s' host='%s', message='%s', date='%s')>" % (
            self.id, self.host, self.message, self.date)

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

def get_logs():
    session = session_factory()
    log_query = session.query(Log)
    session.close()
    return log_query.all()