const fs = require('fs/promises');

function isNameInFile(name, fileToSearch) {
	const pendingPromise = fs
		.readFile(fileToSearch, 'utf8')
		.then((data) => {
			const searchInfo = {
				searchTerm: name,
				isInFile: data.includes(name)
			};
			return searchInfo;
		})
		.catch((err) => {
			const searchInfo = {
				searchTerm: name,
				isInFile: false
			};
			return searchInfo;
		});

	return pendingPromise;
}

module.exports = isNameInFile;
