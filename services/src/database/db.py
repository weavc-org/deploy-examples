import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import SharedConfig

config = SharedConfig()
engine = create_engine(f"postgresql://{config.database.user}:{config.database.password}@{config.database.address}/{config.database.db}")
_SessionFactory = sessionmaker(bind=engine)

DBBase = declarative_base()

def session_factory():
    DBBase.metadata.create_all(engine)
    return _SessionFactory()

