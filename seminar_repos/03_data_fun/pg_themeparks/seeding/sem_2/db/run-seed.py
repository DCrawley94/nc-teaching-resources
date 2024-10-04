from db.seed import seed
from db.connection import create_connection, close_connection
from db.data.index import data

conn = None
try:
    conn = create_connection()
    seed(conn, **data)
except Exception as e:
    print(e, "<<<")
finally:
    if conn:
        close_connection(conn)
