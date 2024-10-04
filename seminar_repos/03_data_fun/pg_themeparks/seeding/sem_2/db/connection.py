from pg8000.native import Connection
import os

DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]


def create_connection():
    conn = Connection(DB_USER, database="nc_games", password=DB_PASS)
    return conn


def close_connection(conn):
    conn.close()
