import pg8000.native


def connect_to_db():
    # creates a connection to database
    return pg8000.native.Connection("danika", database="nc_games")
