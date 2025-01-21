from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re

from db.connection import create_connection, close_connection
from pprint import pprint


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/healthcheck":
            # prepare response
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            # prepare response body
            data = json.dumps({"message": "All good 👍"})

            # write body to response
            self.wfile.write(data.encode("utf-8"))

        # GET /api/games/:game_id

        # Conditional check the path
        if re.search(r"/api/games/\d+", self.path):
            # Pull game id from url
            GAME_BY_ID_REGEX = re.compile(r"/api/games/(\d+)")
            regex_match = re.match(GAME_BY_ID_REGEX, self.path)
            game_id = regex_match.group(1)

            # Set up DB connection
            conn = create_connection()

            # Get games data for given id
            get_game_by_id_query = """
            SELECT * FROM games
            WHERE game_id = :game_id;
            """
            game_data = conn.run(get_game_by_id_query, game_id=game_id)[0]
            columns = [col["name"] for col in conn.columns]

            # Manipulate returned row to match specification

            # for loop/range
            response_body = {"game": {}}
            for i in range(len(columns)):
                column = columns[i]
                value = game_data[i]
                response_body["game"][column] = value

            # response_body = {"game": dict(zip(columns, game_data))}

            # status code
            self.send_response(200)
            # headers
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            # write to response
            # convert response dict into json
            self.wfile.write(json.dumps(response_body).encode("utf-8"))

    def do_POST(self):
        if self.path == "/api/games":
            content_length = int(self.headers["Content-Length"])
            request_body = self.rfile.read(content_length).decode("utf-8")

            pprint(request_body)


server_address = ("", 8000)

with HTTPServer(server_address, Handler) as httpd:
    httpd.serve_forever()
