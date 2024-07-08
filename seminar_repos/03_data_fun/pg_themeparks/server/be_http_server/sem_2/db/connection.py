import pg8000.native


def create_connection():
    return pg8000.native.Connection('danika', database="nc_games")