const isNameInFile = require('..');

describe('isNameInFile', () => {
	test('returns a promise', () => {
		expect(
			typeof isNameInFile('Homer Simpson', './data/simpsons.txt').then
		).toBe('function');
	});
	test.skip('promise resolves with output confirming that given name IS in file', () => {
		const nameToSearch = 'Ned Flanders';
		return isNameInFile(nameToSearch, './data/simpsons.txt').then((data) => {
			expect(data.searchTerm).toBe(nameToSearch);
			expect(data.isInFile).toBe(true);
		});
	});
	test.skip('promise resolves with output confirming that given name IS NOT in file', () => {
		const nameToSearch = 'Seymour Skinner';
		return isNameInFile(nameToSearch, './data/simpsons.txt').then((data) => {
			expect(data.searchTerm).toBe(nameToSearch);
			expect(data.isInFile).toBe(false);
		});
	});
	test.skip('if file cannot be found then promise should resolves with output confirming that given name IS NOT in file', () => {
		const nameToSearch = 'Seymour Skinner';
		return isNameInFile(nameToSearch, './not/a/file.txt').then((data) => {
			expect(data.searchTerm).toBe(nameToSearch);
			expect(data.isInFile).toBe(false);
		});
	});
});

// testcases:

// Ned Flanders - Yes

// Seymour Skinner - No

// Wrong file - No
