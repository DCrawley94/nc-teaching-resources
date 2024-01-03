# Requests That Involve a Body

## Learning Objectives

- Know how to handle a Post request to a HTTP server
- Be able to access useful data from the request object
- Use the response object methods to build and send a response.

## Intro - Figjam

Recap of the Client and Server relationship:

A client is an application making a request for external data - typically a browser.

A server is any program listening for requests on a computer port, that then processes these requests and sends responses accordingly.

## Introduce Repo

- Show the data that will be used
- Show the file that will contain our server
- Show the task md file

Point out that the server has already been created and there is a pre-existing endpoint for GET requests to the same endpoint that we will be using for the POST requests.

## Insomnia

Show how we can set up the POST request by editing the body.

Body:

```json
{
	"artworkId": 5,
	"title": "Starry Night",
	"artistId": 4,
	"worthInDollars": 15000000
}
```

Show that the body will be a JSON object with the same properties as the ones in the `artworks.json` file.

**Pick a student to help write the conditional logic for the POST request.**

Once that is done log a message to check that the conditional logic is correct.

## Building up the body

Refresh students memories on previous knowledge:

- Data is sent across the internet in packets
- Therefore we won't have access to everything on the body straight away
- We need to build up the body by concatenating the strings

**Ask students if anyone knows the `request` method we can use to do this**

```js
let body = '';
request.on('data', (packet) => {
	body += packet;
});
```

**Ask students if anyone knows how we can access the completed body**

```js
request.on('end', () => {
	console.log(body);
});
```

**Ask students what data type the body will be**

**How can we convert the string into something more useful?**

```js
request.on('end', () => {
	const postedArtwork = JSON.parse(body);
});
```

## Pseudocode solution

Ask students for some help writing pseudocode for the logic of adding it to a file.

Possible questions to ask:

- We need to add a new object into the JSON array, what would be the first thing we need to do?

**If students say just write the file straight away talk about why this won't work - can also put this to them as a question instead**

- Once we've read the file, what data type is the data we get back? How to convert to more useful JS?

- How to add our artwork to the current artworks array?

- What do we do with the new array? Do we need to do anything to it before we can write it? (stringify)

- once the file is written what do we need to do?

- What would be an appropriate status code?

Possible pseudocode:

```js
// read current file contents
// parse file contents
// add new artwork object to the array
// write file with stringified array
// build up response with 201 status code and added artwork
// send response
```

---

**🏁 CHECKPOINT 🏁**

---

## Write solution with help from pseudocode.

Something like this:

```js
request.on('end', () => {
	const artworkToPost = JSON.parse(body);
	fs.readFile(`${__dirname}/data/artworks.json`, 'utf-8')
		.then((artworks) => {
			const parsedArtworks = JSON.parse(artworks);
			const artWorksWithAddedArt = [...parsedArtworks, artworkToPost];
			return fs.writeFile(
				`./data/artworks.json`,
				JSON.stringify(artWorksWithAddedArt, null, 2)
			);
		})
		.then(() => {
			response.statusCode = 201;
			response.setHeader('Content-Type', 'application/json');
			response.write(JSON.stringify({ addedArtwork: artworkToPost }));
			response.end();
		})
		.catch((err) => {
			console.log({ err });
		});
});
```

Can show how to use third argument of `JSON.stringify` to format the file nicely:

```js
JSON.stringify(artWorksWithAddedArt, null, 2);
```

**don't go into this in depth, encourage students to look at docs for more info**

Show this working at the end

## Recap and discussion about artwork ID

Talk through the logic

Discuss why needed the client to give an ID is not great code:

- ID should be unique and client won't know which ID to use

Ask for suggestions on how to do this programmatically.
