import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DECIMAL
from sqlalchemy import create_engine
from sql.database import SessionLocal
import os
import csv
import random as rnd
import string


Base = declarative_base()


# DATABASE = os.environ['DATABASE']
# DB_USER = os.environ['DB_USER']
# DB_PASSWORD = os.environ['DB_PASSWORD']
# DB_NAME = os.environ['DB_NAME']
# DB_HOST = os.environ['DB_HOST']
# POSTGRESQL_CONFIG = f"{DATABASE}+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


POSTGRESQL_CONFIG = os.environ['POSTGRESQL_CONFIG']

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
        locs = []
        loc_zips = []
        for i in range(20):
            locs.append(rnd.randint(1, 2000))
        i = 0
        with SessionLocal() as db:
            with open('./sql/uszips.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data = Location()
                    data.zip = row['zip']
                    data.lat = row['lat']
                    data.lng = row['lng']
                    data.city = row['city']
                    data.state = row['state']
                    db.add(data)
                    if i in locs:
                        loc_zips.append(row['zip'])
                    i += 1
            for i in range(20):
                datacar = Car()
                number = ''
                for j in range(4):
                    a = rnd.randint(0, 9)
                    number = number + str(a)
                b = rnd.choice(string.ascii_uppercase)
                number = number + b
                datacar.loc = loc_zips[i]
                datacar.numb = number
                datacar.tonnage = rnd.randint(1, 1000)
                db.add(datacar)
            db.commit()
    elif sys.argv[1] == 'dropdb':
        drop_tables()
