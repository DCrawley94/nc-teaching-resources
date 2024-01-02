const http = require('http');
const fs = require('fs/promises');

const server = http.createServer((request, response) => {
	const method = request.method;
	const url = request.url;
	//can destructure this

	if (url === '/api/artworks' && method === 'GET') {
		fs.readFile('./data/artworks.json', 'utf-8')
			.then((contents) => {
				const artworks = JSON.parse(contents);
				response.statusCode = 200;
				response.setHeader('Content-Type', 'application/json');
				response.write(JSON.stringify({ artworks: artworks }));
				response.end();
			})
			.catch((err) => {
				console.log(err);
			});
	}

	// Discussion points for /api/artworks/:artworkId

	// possible psuedocode:
	// check the url matches the pattern of /api/artworks/:artworkId and method is GET
	//     // Could use .endsWith
	//     // Could use regex like: if (/^\/api\/artworks\/\d+$/.test(url) && method === "GET")
	// if it does, extract the id from the url
	//     // could use split("/")
	//     // or regex .match()
	// use fs to read the contents of the artworks.json data file
	// parse the contents to JS
	// use the extracted artworkId to filter out the correct artwork
	// contruct the response
	// send the response

	//here's a solution if everyone's far enough ahead

	if (/^\/api\/artworks\/\d+$/.test(url) && method === 'GET') {
		const providedArtworkId = url.split('/')[3];
		fs.readFile('./data/artworks.json', 'utf-8')
			.then((contents) => {
				const allArtworks = JSON.parse(contents);
				console.log(allArtworks);

				const artworkWithId = allArtworks.filter((artwork) => {
					return artwork.artworkId == providedArtworkId; //i've used a == because one's a string one's a number
				});
				response.statusCode = 200;
				response.setHeader('Content-Type', 'application/json');
				response.write(JSON.stringify({ artwork: artworkWithId }));
				response.end();
			})
			.catch((err) => {
				console.log({ err });
			});
	}
});

server.listen(9090, (err) => {
	if (err) {
		console.log(err);
	} else {
		console.log('Server listening on port: 9090');
	}
});
