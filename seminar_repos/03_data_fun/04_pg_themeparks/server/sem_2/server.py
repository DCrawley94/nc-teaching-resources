from http.server import BaseHTTPRequestHandler, HTTPServer
from db.connection import create_connection, close_connection
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/reviews":
            conn = create_connection()

            query_result = conn.run("SELECT * FROM reviews;")
            games_columns = [col["name"] for col in conn.columns]

            close_connection(conn)

            formatted_games_data = []

            for game in query_result:
                game = {games_columns[i]: game[i] for i in range(len(games_columns))}
                formatted_games_data.append(game)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            data = json.dumps({"reviews": formatted_games_data})

            self.wfile.write(data.encode("utf-8"))


server_address = ("", 8000)
with HTTPServer(server_address, Handler) as httpd:
    httpd.serve_forever()
