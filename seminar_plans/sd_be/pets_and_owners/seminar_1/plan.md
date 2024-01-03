# Features of Express

## Learning Objectives

- Be able to create an express app
- Know how to use parametric endpoints in express
- Understand when and why query parameters can be useful

## Intro

Introduce repo, highlight the following:

- Creating a server with `express()`.
- Server listening on port 9090.
- Band data stored in individual files in
- Endpoint `/api/bands` set up to accept `GET` requests.

## Introduce Task

Discuss the tasks for the seminar.

**Start noting down a possible endpoint `/api/bands`**

**talk about how we could hardcode a different endpoint for each band**

**ask how we could make it a bit more programmatic**

Hopefully they suggest parametric and we can end up with `/api/bands/:id/songs`.

## Start solution

Set up an Insomnia request, briefly discuss that I'm using `nodemon` so don't need to constantly stop and start the server.

Demonstrate how we can set up the parametric endpoint and access the params.

```js
app.get('/api/band/:id/songs', (req, res) => {
	console.log(req.params);
});
```

**Highlight that params is an object and make the link between the name of the param and the key in the object**

Ask students for pseudocode to solve the rest of the problem - mention that the ID corresponds to the file name.

Possible pseudocode:

```js
// readFile and get file contents
// parse file
// access songs property
// build and send response
```

Ask students to guide me through solution.

End up with something like this:

```js
app.get('/api/band/:id/songs', (req, res) => {
	const bandId = req.params.id;

	fs.readFile(`./data/bands/${bandId}.json`, 'utf-8').then((fileContents) => {
		const parsedFile = JSON.parse(fileContents);
		const songs = parsedFile.songs;

		res.status(200).send({ songs: songs });
	});
});
```

---

**🏁 CHECKPOINT 🏁**

Show endpoint working and ask if anyone needs clarification.

---

## Discuss second part of the solution

We ONLY want songs that are not explicit

Show data and that the songs have a key that tells us if it's explicit or not - therefore this is something we can manage.

However how could we write the url for the endpoint.

**Ask students for suggestions - they will likely suggest an extra part of the path - some may suggest a query**

Explain why a query could be useful in ths case as we're still fundamentally doing the same thing and we can dry up the code by using queries.

Shoe how to write a query URL in insomnia:

`/api/bands/1/songs?explicit=false`

Show how that can be accessed:

```js
app.get('/api/band/:id/songs', (req, res) => {
	console.log(req.query);
});
```

Again point out the key-value link to the query param - **explain that req.query is always going to be an object but will only have properties if there are queries!**

If there's time ask students to help with pseudocode.

Possible pseudocode:

```js
// pull of the query value for explicit
// check if it is there - truthiness as it will otherwise be undefined
// filter songs according to the value of explicit key
// build and send response as usual
```
