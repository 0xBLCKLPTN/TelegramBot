from datetime import datetime

from db.db import Base
from sqlalchemy import Column, DateTime, Integer, String, BigInteger


class Admins(Base):
    __tablename__ = 'Admins'

    id = Column(Integer, primary_key=True)
    username = Column(String, default= None)
    user_id = Column(String)
    created = Column(DateTime, default=datetime.utcnow)


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    
    FirstName = Column(String)
    MiddleName = Column(String)
    LastName = Column(String)
    
    username = Column(String)
    user_id = Column(Integer)
    phone_number = Column(String)
    email = Column(String)

    cookies_file = Column(String, default= None)
    company_id = Column(Integer, default = None)
    recomendations_file = Column(String, default = None)
    list_of_products_file = Column(String, default = None)

    company_name = Column(String)
    revenue = Column(BigInteger)
    added = Column(DateTime, default = datetime.utcnow)
    last_buy = Column(DateTime, default = None)

