from datetime import date, datetime

from .log import Log
from .db import session_factory

def create_log(host: str, message: str):
    session = session_factory()
    m = Log(host=host, message=message, date=datetime.now())
    session.add(m)
    session.commit()
    session.close()

def get_logs():
    session = session_factory()
    log_query = session.query(Log)
    session.close()
    return log_query.all()