const getMiddleChar = require('../getMiddleChar');

describe('getMiddleChar', () => {
	test('returns given string if string length < 3', () => {
		expect(getMiddleChar('')).toBe('');
		expect(getMiddleChar('a')).toBe('a');
		expect(getMiddleChar('ab')).toBe('ab');
	});
	test('returns the middle character of an odd length string', () => {
		expect(getMiddleChar('abc')).toBe('b');
	});
});
