from http.server import BaseHTTPRequestHandler, HTTPServer
from db.connection import create_connection
import json


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

        # TODO: POST /api/games
        


server_address = ('', 8000)
with HTTPServer(server_address, Handler) as httpd:
    httpd.serve_forever()