const fs = require('fs/promises');

function isNameInFile(name, fileToSearch) {
	return fs.readFile(fileToSearch, 'utf-8').then((data) => {
		// do stuff
	});
}

module.exports = isNameInFile;
