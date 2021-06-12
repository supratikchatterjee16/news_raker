import pandas
import logging

from datetime import datetime
from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, ForeignKey, create_engine
# NOTE : LargeBinary refers to Blob. Can be used in SQLite, PostgreSQL,
from sqlalchemy.ext.declarative import declarative_base

from . import config

db_src = "sqlite:///:memory:" if not config['DATABASE_URI'] else config['DATABASE_URI']
print(db_src)
engine = create_engine(db_src, echo = True)

Base = declarative_base()

class Source(Base):
    __tablename__ = "sources"
    id = Column(Integer, primary_key = True)
    name = Column(String, unique=True, nullable=False)
    url = Column(String, unique=True, nullable=False)
    # load_sources is tasked with loading csv data from
    # a particular file into the table 'sources'
    @staticmethod
    def load(path):
        sources = pandas.read_csv(path, names=["name", "url"])
        with engine.connect() as connection:
            sources.to_sql('sources', connection, if_exists='replace', index=True, index_label='id')
    @staticmethod
    def get_all():
        sources = pandas.DataFrame()
        with engine.connect() as connection:
            sources = pandas.read_sql('sources', connection, index_col=['id'])
        return sources

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key = True)
    source = Column(Integer, ForeignKey('sources.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)

class ArticleParts(Base):
    __tablename__ = "article_parts"
    id = Column(Integer, primary_key = True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    article_part = Column(String)
try:
    Base.metadata.create_all(engine, checkfirst=True)
except:
    pass
