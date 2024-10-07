from http.server import BaseHTTPRequestHandler, HTTPServer
import json


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


server_address = ("", 8000)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()
