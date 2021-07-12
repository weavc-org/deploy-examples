from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:password@postgres:5432/service-test-db')
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()

