from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DB_CONF = settings.DATABASES['default']
# DB_CONF = {"USER": "bottomv1", "PASSWORD": "bottom12345", "HOST": "20.124.237.246", "NAME": "bottompostgres"}
# DATABASE_URL = f"postgresql://{DB_CONF['USER']}:{DB_CONF['PASSWORD']}@{DB_CONF['HOST']}:5432/{DB_CONF['NAME']}"

# DATABASE_URL = 'postgresql://non-prod-rw-access:devpassword@34.133.12.107/combined-qa-db'


# engine = create_engine(DATABASE_URL, pool_pre_ping=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


class Settings(BaseSettings):
    appName: str = "Team Management project"

    openapi_url: str = '/api/phylax/openapi.json'

# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

#
# from pymongo import MongoClient
# import settings
#
# client = MongoClient(settings.mongodb_uri, settings.port)
# db = client[customerdata]
