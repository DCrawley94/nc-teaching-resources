const fs = require('fs');

function countTheWorlds(cb) {
	fs.readFile('./data/helloWorld.txt', 'utf-8', (err, data) => {
		// readfile goes to node api
		if (err) {
			// do something with err
			cb(err);
		} else {
			//  do something with the data
			const patternToMatch = /world/g;
			const matches = data.match(patternToMatch);

			cb(null, matches.length);
		}
	});
	//  do any other synchronous stuff
}

module.exports = countTheWorlds;
