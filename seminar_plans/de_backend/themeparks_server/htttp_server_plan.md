# Python HTTP server

## Introduce the Repo

Explain that it's the same repo I was working in on Friday:

- we're still working with the `nc_games` database > show schema
- the data is fully seeded
- show plan for the session:

Two endpoints:

- GET /api/games/:game_id
- POST /api/games

## Reminder of server setup:

[HTTP Server Docs](https://docs.python.org/3/library/http.server.html#http.server.HTTPServer)

- imported `BaseHTTPRequestHandler` and `HTTPServer` from the built-in http library
- defined a class `Handler` that inherits from the `BaseHTTPRequestHandler`
- down below I've created a `server_address` tuple, I've passed this and the `Handler` class to HTTPServer - this creates the server. I've then invoked `serve_forever` to get the server listening

```py
server_address = ('', 8000)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()
```

- **the empty string in the server_address tuple represents the IP address of the server, in this case localhost**
- When run, this server will listen for incoming requests on http://localhost:8000

Point out that there is already one endpoint - healthcheck

Demo it working by using Insomnia:

- show that with insomnia we can easily make http request to the localhost
- explain that it will also come in handy when make POST requests

## First endpoint - get game by ID

- GET /api/games/:game_id

While showing the healthcheck endpoint pick someone to help write a bit of pseudocode to break down what we need to do for our solution.

Possible pseudocode:

```py
# check url - how do we match the url when the ID could be anything - Regex?
# Query the DB to get the game with correct ID - what format will this return?
# Format response into more something more helpful
# Build up response and send
```

## Starting writing out code:

- `import re` - we'll need this for checking the path
- `from db.connection import conn` - we'll need this for querying the DB
- `GET_GAME_BY_ID_REGEX = re.compile(r"/api/games/\d+")` - define a REGEX for matching the path

Pick on people as I'm working through the solution, thing like:

- How can I match any number of digits with regex?
-

Possible solution:

```py
# check url - how do we match the url when the ID could be anything - Regex?
if re.fullmatch(GET_GAME_BY_ID_REGEX, self.path): # fullmatch will match the whole string/could possibly use normal match instead
    # Get game ID from url
    game_id = re.search(r"\d+", self.path)[0]

    # Query the DB to get the game with correct ID - what format will this return?
    query_result = conn.run("""
    SELECT *
    FROM games
    WHERE game_id = :game_id;
    """, game_id = game_id)[0]

    game_columns =  [col['name'] for col in conn.columns]

    # Format response into more something more helpful
    game_data = {}

    for i in range(len(game_columns)):
        game_data[game_columns[i]] = query_result[i]

    # Build up response and send
    # prepare response
    self.send_response(200)
    self.send_header('Content-Type', 'application/json')
    self.end_headers()

    # prepare response body
    response_body = json.dumps({"game": game_data})

    # write body to response
    self.wfile.write(response_body.encode("utf-8"))

```

## Depending on time: Pseudocode the POST endpoint

- POST /api/games

Possible pseudocode:

```py
# check url - only POST for now but there could easily be more
# extract request body - I'm gonna expect data to be there for every column for simplicity
# Query the DB to INSERT the game - and return the newly inserted data to be sent back
# Format response into more something more helpful
# Build up response and send
```

## Glossary

`rfile` : The "input stream" - allows us to read data sent to us by the client

`wfile` : The "output stream" - allows us to write a response back to the client - adherence to HTTP protocol is important to allow it to work with HTTP clients
