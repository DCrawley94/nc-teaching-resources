# OPTIONAL SEMINAR: Creating a `pg8000` Connection object

## Refresher

> What information do we need in order to set up a Connection to a postgres database?

- user
- database
- password (On MacOS this is handled for us behind the scenes, however if we were connecting to a remote database then it would still be needed)

## Multiple Options

For all of the below we can prove it working with:

```py
print(conn.run("SELECT 1;"))
```

### Passing credentials on the command line

```sh
DB_USER='danika' DB_PASS='password123' DB_DATABASE='nc_games' python db/connection.py
```

```py
from pg8000.native import Connection

# from dotenv import load_dotenv
import os

# load_dotenv()

DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_DATABASE = os.environ["DB_DATABASE"]


def create_connection():
    conn = Connection(DB_USER, database=DB_DATABASE, password=DB_PASS)
    return conn


def close_connection(conn):
    conn.close()


conn = create_connection()
print(conn.run("SELECT 1;"))
```

## Using python-dotenv

```sh
python db/connection.py
```

```py
from pg8000.native import Connection
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_DATABASE = os.environ["DB_DATABASE"]


def create_connection():
    conn = Connection(DB_USER, database="nc_games", password=DB_PASS)
    return conn


def close_connection(conn):
    conn.close()
```
