import youngVoice.config as config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, String, DateTime, Text, desc, or_

DB_CONN_STRING = 'mysql+mysqldb://%s:%s@localhost/%s?charset=utf8' % (config.DB_USER, config.DB_PASS, config.DB_NAME)
engine = create_engine(DB_CONN_STRING, echo=True)

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
session = Session()
Base = declarative_base()
Base.query = Session.query_property()
Base.metadata.create_all(bind=engine)

