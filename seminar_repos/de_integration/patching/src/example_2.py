from pg8000.native import Connection
from pg8000.exceptions import DatabaseError


def get_games():
    '''
    Function will get game from the nc_games database and return
    a list in the following form:

    [
      {
        games_id: int
        game_title: string
        release_year: int
        image_url: string
        console_name: string
      }, ...
    ]
    '''
    try:
        print(Connection.run)
        conn = Connection(
            host='localhost',
            user='danika',
            database='nc_games'
        )
        print(conn)
        print(dir(conn))
        print(conn.run, '  1')
        # print(conn, type(conn), '1')
        print(conn.run, '  2')
        print(type(conn.run), '   3')
        rows = conn.run('SELECT * FROM games;')
        print(rows, 'rows')
        columns = [
            'games_id', 'game_title', 'release_year', 'image_url', 'console_name']
        response = []

        for row in rows:
            formatted_row = {columns[i]: val for i, val in enumerate(row)}
            response.append(formatted_row)

        return response
    except DatabaseError:
        return "Error querying the database"