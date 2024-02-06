from pg8000.native import Connection


def get_games():
    '''
    Function will get superheroes from the marvel database and return
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

    conn = Connection(
        host='localhost',
        user='danika',
        database='nc_games'
    )
    rows = conn.run('SELECT * FROM games;')

    columns = ['games_id', 'game_title',
               'release_year', 'image_url', 'console_name']

    response = []

    for row in rows:
        formatted_row = {columns[i]: val for i, val in enumerate(row)}
        response.append(formatted_row)

    return response
