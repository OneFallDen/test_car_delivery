import psycopg

from sql import database as db


def connection():
    con = psycopg.connect(
        database=db.DATABASE,
        user=db.DB_USER,
        password=db.DB_PASSWORD,
        host=db.DB_HOST,
        port=8000
    )
    return con
