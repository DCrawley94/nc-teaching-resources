# Recap of repo so far

## Learning Objectives

- Understand how the different components of our API work together as a complete application.
- Recap of TDD of a new endpoint from start to finish.

## Intro

Take a look at the diagram showing how the different DB files are used.

Explain purposes and how this is happening in the repo.

**Ask students how Node Postgres knows which database to connect to**

- PGDATABASE environment variable

**Where is the PGDATABASE env variable being set?**

- .env files

**How does the connection file know which .env file to use?**

- Uses the value of the NODE_ENV env variable to work out which file to use

---

Take a look at the diagram showing how the Express API files are linked together.

- controllers job is to handle the request and response
- models job is to interact with the DB

- assuming a successful request the controller will send back the data from the model to client.

- If there are any errors the controller will instead pass those to our error handling middleware functions - these will determine what kind of response and status code to send back to the client.

---

Ask student if there's any particular parts of the Backend repo that they struggle to understand:

Possible topics:

- seed files
- .env files
- connection
- mvc
- testing > will be covered anyway
- error handling > will be covered anyway

## Walkthrough new endpoint - Post Review

Explain how the post review endpoint works

client request > app.js > controllers > models > controllers > response to client

```json
// POST /api/reviews

// Review body:
{
	"username": "fola",
	"game_id": 1,
	"comment": "blah blah blah",
	"rating": 5
}
```

Ask students what could go wrong?

- malformed body - missing game_id - 404
- Valid but non-existant game_id - 404

```js
// in error handler

else if (err.code === '23503') {
		res.status(404).send({ msg: 'Not Found' });
	}
```

- invalid game_id - 400
