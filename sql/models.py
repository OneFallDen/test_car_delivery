import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DECIMAL
from sqlalchemy import create_engine
import os


Base = declarative_base()


DATABASE = os.environ['DATABASE']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']
DB_HOST = os.environ['DB_HOST']
POSTGRESQL_CONFIG = f"{DATABASE}+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


engine = create_engine(POSTGRESQL_CONFIG, echo=True, future=True)


class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True, index=True)
    numb = Column(String(5), nullable=False)
    loc = Column(String(5), nullable=False)
    tonnage = Column(Integer, nullable=False)


class Cargo(Base):
    __tablename__ = 'cargo'

    id = Column(Integer, primary_key=True, index=True)
    pick_up = Column(String(5), nullable=False)
    delivery = Column(String(5), nullable=False)
    weight = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    zip = Column(String(5), nullable=False)
    lat = Column(DECIMAL, nullable=False)
    lng = Column(DECIMAL, nullable=False)


def create_db_and_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    if sys.argv[1] == 'createdb':
        create_db_and_tables()
    elif sys.argv[1] == 'dropdb':
        drop_tables()
