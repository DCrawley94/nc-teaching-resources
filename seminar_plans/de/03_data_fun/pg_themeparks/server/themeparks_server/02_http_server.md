# Python HTTP server

Figjam: https://www.figma.com/file/Ps3GlZgxKAM84cLEVmiSeZ/HTTP-Servers?type=whiteboard&t=XBS1TZhMYdVoPrpT-6

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
# Format response into more something more helpful - we will need column names - we can hardcode these but is there a better way?
# Build up response and send
```

## Starting writing out code:

- `import re` - we'll need this for checking the path - might not be nece
- `from db.connection import conn` - we'll need this for querying the DB
- `GET_GAME_BY_ID_REGEX = re.compile(r"/api/games/(\d+)")` - define a REGEX for matching the path

Pick on people as I'm working through the solution, thing like:

- How can I match any number of digits with regex?
- how can I pull the game id from the url?
- Ask someone to guide me through writing the SQL
- How should we deal with column names? We can hardcode these but is there a better way?
- WHat response code should I send?
- What content type should I specify?
- What dod I need to do once I've finished setting headers? - end headers
- What data type should the response body be? - string therefore `json.dumps`
- What encoding should it be in? - utf-8, should default to that but we can make sure with the `.encode` method

Possible solution:

**TRY TO SHOW ZIP FUNCTION FOR BUILDING RESPONSE**

Possible solution:

```py
# check url - how do we match the url when the ID could be anything - Regex?
if re.match(GET_GAME_BY_ID_REGEX, self.path):
    # Get game ID from url
    game_id = int(re.match(GET_GAME_BY_ID_REGEX, self.path).group(1))

    # Query the DB to get the game with correct ID - what format will this return?
    conn = create_connection()

    query_result = conn.run("""
    SELECT *
    FROM games
    WHERE game_id = :game_id;
    """, game_id = game_id)[0]

    game_columns =  [col['name'] for col in conn.columns]

    # Format response into more something more helpful
    game_data = dict(zip(game_columns, query_result))

    # IF zip doesn't work can use this
    # for i in range(len(game_columns)):
    #     game_data[game_columns[i]] = query_result[i]

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

Possible solution:

```py
def do_POST(self):
    if self.path == '/api/games':
        # This gets the size of data
        content_length = int(self.headers['Content-Length'])
        # This gets the data itself
        request_body = self.rfile.read(content_length).decode(
            'utf-8')

        # parse request body
        new_game = json.loads(request_body)

        insert_query_str = """
        INSERT INTO games
        (game_title, release_year, console_name, image_url)
        VALUES
        (:game_title, :release_year, :console_name, :image_url)
        RETURNING *;
        """

        inserted_game = conn.run(insert_query_str, **new_game)[0]

        # More formatting of data returned from the query
        game_columns = [col['name'] for col in conn.columns]
        formatted_game = {game_columns[i]: inserted_game[i]
                          for i in range(len(game_columns))}

          # prepare response
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        # prepare response body
        data = json.dumps({"ride": formatted_game})

        # write body to response
        self.wfile.write(data.encode("utf-8"))
```

## Glossary

`rfile` : The "input stream" - allows us to read data sent to us by the client

`wfile` : The "output stream" - allows us to write a response back to the client - adherence to HTTP protocol is important to allow it to work with HTTP clients
