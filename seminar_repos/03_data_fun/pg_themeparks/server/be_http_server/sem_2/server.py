from http.server import BaseHTTPRequestHandler, HTTPServer
from db.connection import create_connection
import json
import re

GET_GAMES_BY_ID_REGEX = re.compile(r"/api/games/(\d+)")
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

        # TODO: GET /api/games/:game_id
        if GET_GAMES_BY_ID_REGEX.match(self.path):
             # Get game ID
            game_id = GET_GAMES_BY_ID_REGEX.match(self.path).group(1)

            # Get game data - query DB using game ID
            query_string = """
            SELECT * FROM games
            WHERE game_id = :id;
            """
            conn = create_connection()
            result = conn.run(query_string, id = game_id)
            conn.close()
            
            # Format data returned
            columns = [column['name'] for column in conn.columns]
            game_data = dict(zip(columns, result[0]))

            response = {'game': game_data}

            # Convert response into JSON
            response_body = json.dumps(response)

            # Write headers and send response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            self.wfile.write(response_body.encode("utf-8"))

        # TODO: POST /api/games
    def do_POST(self):
        content_length =  int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length).decode('utf-8')

        new_game = json.loads(request_body)

        # Insert query - insert new game into DB - RETURNING

        # Use data from the Insert query

        # Format data - use conn.columns again

        # Convert data to JSON

        # create response - write headers

        # send response


server_address = ('', 8000)
with HTTPServer(server_address, Handler) as httpd:
    httpd.serve_forever()