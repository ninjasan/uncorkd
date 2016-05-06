"""Contains database session to be used for the whole application """
__author__ = 'poojm'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from uncorkd.data.models import Base

engine = create_engine('sqlite:///uncorkd.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
