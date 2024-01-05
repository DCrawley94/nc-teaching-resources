const moveToManchester = require('..');

describe('moveToManchester', () => {
	test('when passed an empty array - returns an empty array', () => {
		expect(moveToManchester([])).toEqual([]);
	});
	test('updates location for single person in array', () => {
		const testInput = [{ name: 'Simon', age: 21, location: 'Leeds' }];
		const expectedOutput = [{ name: 'Simon', age: 21, location: 'Manchester' }];

		expect(moveToManchester(testInput)).toEqual(expectedOutput);
	});
	test('updates location for every person in given array', () => {
		const testInput = [
			{ name: 'Mick', age: 21, location: 'Liverpool-ish' },
			{ name: 'August', age: 21, location: 'Ancoats' },
			{ name: 'Chon', age: 21, location: 'Somewhere else' }
		];
		const expectedOutput = [
			{ name: 'Mick', age: 21, location: 'Manchester' },
			{ name: 'August', age: 21, location: 'Manchester' },
			{ name: 'Chon', age: 21, location: 'Manchester' }
		];

		expect(moveToManchester(testInput)).toEqual(expectedOutput);
	});
	test('should not mutate input', () => {
		const testInput = [
			{ name: 'Mick', age: 21, location: 'Liverpool-ish' },
			{ name: 'August', age: 21, location: 'Ancoats' },
			{ name: 'Chon', age: 21, location: 'Somewhere else' }
		];

		moveToManchester(testInput);

		// does the input still look the same?

		expect(testInput).toEqual([
			{ name: 'Mick', age: 21, location: 'Liverpool-ish' },
			{ name: 'August', age: 21, location: 'Ancoats' },
			{ name: 'Chon', age: 21, location: 'Somewhere else' }
		]);
	});
	test('output should have a different reference to input', () => {
		const testInput = [
			{ name: 'Mick', age: 21, location: 'Liverpool-ish' },
			{ name: 'August', age: 21, location: 'Ancoats' },
			{ name: 'Chon', age: 21, location: 'Somewhere else' }
		];

		const output = moveToManchester(testInput);

		expect(output).not.toBe(testInput);

		testInput.forEach((person, i) => {
			expect(person).not.toBe(output[i]);
		});
	});
});
