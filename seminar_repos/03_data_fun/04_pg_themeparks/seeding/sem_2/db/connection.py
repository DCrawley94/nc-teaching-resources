from pg8000.native import Connection
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_DATABASE = os.environ["DB_DATABASE"]


def create_connection():
    return Connection(DB_USER, database=DB_DATABASE, password=DB_PASS)


def close_connection(conn):
    conn.close()
