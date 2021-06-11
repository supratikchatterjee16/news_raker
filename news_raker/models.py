import pandas

from datetime import datetime
from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, ForeignKey
# NOTE : LargeBinary refers to Blob. Can be used in SQLite, PostgreSQL,
from sqlalchemy.ext.declarative import declarative_base

from . import config

engine = create_engine("sqlite:///:memory:" if not config['DATABASE_URI'] else config['DATABASE_URI'], echo = True)

Base = declarative_base()

class Source(Base):
    __tablename__ = "sources"
    id = Column('id')
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    # load_sources is tasked with loading csv data from
    # a particular file into the table 'sources'
    @staticmethod
    def load_sources(path):
        sources = pandas.read_csv(path)
        with engine.connect() as connection:
            sources.to_sql('sources', connection)

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key = True)
    url = Column(String, unique=True)
    source = Column(String, ForeignKey('sources.name'))
    article_part_0 = Column(String)
    article_part_1 = Column(String)
    article_part_2 = Column(String)
    article_part_3 = Column(String)
    article_part_4 = Column(String)
    article_part_5 = Column(String)
    article_part_6 = Column(String)
    article_part_7 = Column(String)
    article_part_8 = Column(String)
    article_part_9 = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
