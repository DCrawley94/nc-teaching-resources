import pg8000.native
import os

PG_PASSWORD = os.environ['PGPASS']

conn = pg8000.native.Connection(
    'danika', database="nc_games", password=PG_PASSWORD)
