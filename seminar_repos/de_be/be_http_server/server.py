from http.server import BaseHTTPRequestHandler, HTTPServer
from db.connection import conn
import json
import re

GET_GAME_BY_ID_REGEX = re.compile(r"/api/games/\d+")

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

        # check url - how do we match the url when the ID could be anything - Regex?
        if re.fullmatch(GET_GAME_BY_ID_REGEX, self.path):
            # Get game ID from url
            game_id = re.search(r"\d+", self.path)[0]

            # Query the DB to get the game with correct ID - what format will this return?
            query_result = conn.run("""
            SELECT *
            FROM games
            WHERE game_id = :game_id;
            """, game_id = game_id)[0]

            game_columns =  [col['name'] for col in conn.columns]

            print(query_result)
            print(game_columns)

            # Format response into more something more helpful
            game_data = {}

            for i in range(len(game_columns)):
                game_data[game_columns[i]] = query_result[i]

            print(game_data)

            # Build up response and send
            # prepare response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            # prepare response body
            response_body = json.dumps({"game": game_data})

            # write body to response
            self.wfile.write(response_body.encode("utf-8"))


server_address = ('', 8000)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()