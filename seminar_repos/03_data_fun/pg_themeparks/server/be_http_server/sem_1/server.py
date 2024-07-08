from http.server import BaseHTTPRequestHandler, HTTPServer
from db.connection import conn
import json
import re

GET_GAME_BY_ID_REGEX = re.compile(r"/api/games/(\d+)")



class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/healthcheck':
            # prepare response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            # prepare response body
            data = json.dumps({"message": "All good 👍"})

            # write body to response
            self.wfile.write(data.encode("utf-8"))

        # GET /api/games/:game_id
        # - check the endpoint
        if self.path == '/api/games':
            conn = connect_to_db()
            # Get Data and columns
            query_result = conn.run("SELECT * FROM games;")
            # could also hardcode this
            games_columns = [col['name'] for col in conn.columns]

            # Use column names to format data - this is to turn it into list
            #   of dictionaries rather than list of lists - can be skipped over
            formatted_games_data = []

            for game in query_result:
                game = {games_columns[i]: game[i]
                        for i in range(len(games_columns))}
                formatted_games_data.append(game)

            # prepare response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            # prepare response body
            data = json.dumps({"games": formatted_games_data})

            # write body to response
            self.wfile.write(data.encode("utf-8"))
        if re.match(GET_GAME_BY_ID_REGEX, self.path):
            # - extract the game_id from the url
            game_id = int(re.match(GET_GAME_BY_ID_REGEX, self.path).group(1))

            # - query the DB for the game with game_id
            query_result = conn.run("""
            SELECT * FROM games
            WHERE game_id = :game_id
            """, game_id = game_id)[0]

            game_table_columns = [col['name'] for col in conn.columns]

            # - format the data for the response
            formatted_game = dict(zip(game_table_columns, query_result))
        
            # - build and send response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            response_body = json.dumps({"game": formatted_game})

            self.wfile.write(response_body.encode('utf-8'))


server_address = ('', 8000)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()