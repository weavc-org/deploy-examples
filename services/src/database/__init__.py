from datetime import date, datetime

from .log import Log
from .db import session_factory

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