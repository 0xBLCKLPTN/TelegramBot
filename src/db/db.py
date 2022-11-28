"""
db.py - database creator.
Creates a database and returns a session on request.

Written by Daniil ( blcklptn ) Ermolaev.
"""

from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL to our database container
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'  # noqa: E501, WPS326, WPS221

# sqlalchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_database():
    '''
    Creates tables in our database and returns local session.
    '''
    Base.metadata.create_all(bind=engine)
    return SessionLocal()
