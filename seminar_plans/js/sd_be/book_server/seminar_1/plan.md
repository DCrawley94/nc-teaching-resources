# Server Setup and Response Handlers

## Learning Objectives

- Know how to create a basic http server
- Be able to access useful data from the `request` object
- use the `response` object methods to build and send a response.

## Intro - Figjam

Recap of the Client and Server relationship:

A client is an application making a request for external data - typically a browser.

A server is any program listening for requests on a computer port, that then processes these requests and sends responses accordingly.

## Introduce Repo

- Show the data that will be used
- Show the file that will contain our server
- Show the task md file

## Initial Setup

Start with a little reminder of what we're doing:

- using `http` module available through `node`
- using the `createServer` method to set up our server.

Talk through creating this:

```js
const http = require('http');

const server = http.createServer(() => {});
```

Highlight that the `createServer` method take a single argument - a callback function.

Ask students following questions:

- When is this callback function invoked?

A: When the server receives a request.

- What arguments does the callback accept?

A: `request` and `response`

- This server will likely need different functionality depending on the endpoint. Is there any information available to us that would be useful to us?

A: `url` property on request, could also mention `method` for different `http` methods.

**Show the students the request body with `Object.keys()`. Tak about how there is tons of information on there that could be useful but for now the only things we need are `url` and maybe `method`.**

Aim to end up with something like this:

```js
const server = http.createServer((request, response) => {
	// const method = request.method;
	const url = request.url;

	// can destructure this

	if (url === '/api/artworks' /* && method === 'GET'*/) {
		console.log('Time to get some art');
	}
});
```

---

**🏁 CHECKPOINT 🏁**

Ask students if we have everything we need to make a request and see the console log.

- Hopefully they point out that we need to tell the server to listen on a port. If not try running it without and take note of the error.

---

Add in listener, talk about how I'm using a callback that will handle any errors we get when starting the server:

```js
server.listen(9090, (err) => {
	if (err) {
		console.log(err);
	} else {
		console.log('Server listening on port: 9090');
	}
});
```

Run the server file again and see listener console log, send request with Insomnia and see another log from the if block.

## Access the data

Quickfire question for studes:

- We want to get the contents of a file, how can we do that?

A: FS readFile

Gonna make this easy and use promises:

```js
const fs = require('fs/promises');
```

- `readFile` returns a promise, how do we access the resolved value of a promise?

A: `.then`

- How do we deal with a rejected promise?

A: `.catch`

Get something like this:

```js
if (url === '/api/artworks' && method === 'GET') {
	fs.readFile('./data/artworks.json', 'utf-8')
		.then((contents) => {
			console.log(contents);
		})
		.catch((err) => {
			console.log(err);
		});
}
```

- What data type is stored in `contents`?

A: string

- How to we turn that into the correct data type?

A: `JSON.parse()` - get the array

**🎉 WE HAVE THE DATA WE NEED TO SEND 🎉**

## Build up the response

Now we have the data let's build up the response.

### Step 1: Add a Status Code

- What would be an appropriate status code?

A: 200

```js
response.statusCode = 200;
```

### Step 2: Set some Headers

To make this more useful I'm going to add some meta data to our response. This is to tell the client about the nature of the response itself, **not the contents**. It provides a bit more context.

```js
response.setHeader('Content-Type', 'application/json');
```

### Step 3: Add the Body to the response

I'd like the body to be in JSON format. It should be an **object** with a key of **artworks**. On that key it should have the artworks **array**.

I don't technically have to do this, I could just pass any string as the body but this is quite a common format and the key serves as a bit of a label for the data attached.

```js
// Body
// { artworks: [ ...artwork objects]}
```

- What `response` method can we use to attach data to the body?

A: `response.write()`

**However** the `write` method will only accept a string, how can we turn a JavScript object into a string?

A: `JSON.stringify()`

End up with something like this:

```js
if (url === '/api/artworks' && method === 'GET') {
	fs.readFile('./data/artworks.json', 'utf-8')
		.then((contents) => {
			const artworks = JSON.parse(contents);
			response.statusCode = 200;
			response.setHeader('Content-Type', 'application/json');
			response.write(JSON.stringify({ artworks: artworks }));
		})
		.catch((err) => {
			console.log(err);
		});
}
```

- Have we done everything?

A: student may point out the missing `response.end()`. If they don't then send request and explain why it's not worked (hanging).

**`response.send()`???**

---

**🏁 CHECKPOINT 🏁**

Discuss what we've done so far from start to finish

---

## Pseudocode Parametric Endpoint

Remind students of second task in `task.md`.

Write some pseudocode with the students answers to these questions:

- How could we check that the url matches the pattern.

e.g: `/api/artworks/1`, `/api/artworks/7`, `/api/artworks/23`

A: `endsWith` string method (downside: have to have a condition for each digit), `regex` (better option)

- We will likely need to use the ID number. How could we extract it?

A: `split()` or `.match()` with Regex

- Once we've got the ID number how could we get the correct artwork object?

A: `readFile` then `filter` (or something similar)

Possible Pseudocode:

```js
// check the url matches the pattern of /api/artworks/:artworkId and method is GET
//     // Could use .endsWith
//     // Could use regex like: if (/^\/api\/artworks\/\d+$/.test(url) && method === "GET")
// if it does, extract the id from the url
//     // could use split("/")
//     // or regex .match()
// use fs to read the contents of the artworks.json data file
// parse the contents to JS
// use the extracted artworkId to filter out the correct artwork
// construct the response
// send the response
```
