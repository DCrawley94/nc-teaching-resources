from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re

from pprint import pprint

from db.connection import create_connection, close_connection

GAME_BY_ID_REGEX = re.compile(r"/api/games/(\d+)")


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

        # /api/games/:game_id

        # check if url matches - regex - DONE
        if re.match(GAME_BY_ID_REGEX, self.path):
            game_id = re.match(GAME_BY_ID_REGEX, self.path).group(1)

            # get game data for given ID - extract ID from the url
            query_str = """
            SELECT * FROM games
            WHERE game_id = :game_id;
            """

            conn = create_connection()

            game_data = conn.run(query_str, game_id=game_id)[0]
            columns = [col["name"] for col in conn.columns]

            # data formatting
            formatted_game = dict(zip(columns, game_data))

            # setting headers
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            # Converting to JSON
            response_body = json.dumps({"game": formatted_game})

            # send response
            self.wfile.write(response_body.encode("utf-8"))

    def do_POST(self):
        # match the url
        if self.path == "/api/games":
            # extract the request body
            content_length = int(self.headers["Content-Length"])
            request_body = self.rfile.read(content_length).decode("utf-8")

            print(request_body)

        # INSERT SQL query

        # format response
        # set headers
        # Json string
        # write response body


server_address = ("", 8000)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()
