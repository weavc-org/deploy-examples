from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

postgres = os.getenv("POSTGRES_ADDRESS", default="postgres:5432")
password = os.getenv("POSTGRES_PASSWORD", default="password")
user = os.getenv("POSTGRES_USER", default="postgres")
db = os.getenv("POSTGRES_DB", default="deploy-examples")

engine = create_engine(f"postgresql://{user}:{password}@{postgres}/{db}")
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()

