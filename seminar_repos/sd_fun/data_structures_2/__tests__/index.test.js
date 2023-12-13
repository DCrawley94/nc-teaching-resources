const createPlaylist = require('../index');

describe('createPlaylist', () => {
	test('createPlaylist returns an object', () => {
		// Arrange
		const input = 'absolute bangers';
		const expectedOutput = 'object';
		// Act
		const result = createPlaylist(input);

		// Assert
		expect(typeof result).toBe(expectedOutput);
	});
	test('createPlaylist returns object with name property - set to given argument', () => {
		const input = 'absolute bangers';
		const expectedOutput = 'absolute bangers';

		const result = createPlaylist(input);

		expect(result.name).toBe(expectedOutput);
	});
	test('createPlaylist returns object with tracks property - default empty array', () => {
		const expectedOutput = [];

		const result = createPlaylist('abc');

		expect(result.tracks).toEqual(expectedOutput);
	});
	test('addTrack method should add given string to the playlist array', () => {
		const expectedOutput = ['Christmas Hit'];

		const result = createPlaylist();

		result.addTrack('Christmas Hit');

		expect(result.tracks).toEqual(expectedOutput);
	});
});
