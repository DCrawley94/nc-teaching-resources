from http.server import BaseHTTPRequestHandler, HTTPServer
from db.connection import create_connection, close_connection
import json
import re

REVIEWS_BY_ID_REGEX = re.compile(r"/api/reviews/(\d+)")


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

    def do_POST(self):
        if self.path == "/api/games":
            # This gets the size of data
            content_length = int(self.headers["Content-Length"])
            # This gets the data itself
            request_body = self.rfile.read(content_length).decode("utf-8")

            # parse request body
            new_game = json.loads(request_body)

            insert_query_str = """
            INSERT INTO games
            (game_title, release_year, console_name, image_url)
            VALUES
            (:game_title, :release_year, :console_name, :image_url)
            RETURNING *;
            """
            conn = create_connection()

            inserted_game = conn.run(insert_query_str, **new_game)[0]

            # More formatting of data returned from the query
            game_columns = [col["name"] for col in conn.columns]

            close_connection(conn)

            formatted_game = {
                game_columns[i]: inserted_game[i] for i in range(len(game_columns))
            }

            # prepare response
            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            # prepare response body
            data = json.dumps({"ride": formatted_game})

            # write body to response
            self.wfile.write(data.encode("utf-8"))

    def do_DELETE(self):
        if REVIEWS_BY_ID_REGEX.match(self.path):
            # Can solve without regex depending on what students suggest
            review_id = REVIEWS_BY_ID_REGEX.match(self.path).group(1)

            conn = create_connection()

            conn.run(
                "DELETE FROM reviews WHERE review_id = :review_id;", review_id=review_id
            )

            close_connection(conn)

            self.send_response(204)
            # Notice that there's no need to set a content type due to there
            #   being no content to send
            self.end_headers()


server_address = ("", 8000)
with HTTPServer(server_address, Handler) as httpd:
    httpd.serve_forever()
