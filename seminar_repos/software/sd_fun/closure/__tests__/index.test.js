const shoppingList = require('../index');

describe('shoppingList', () => {
	test('shoppingList should return a function', () => {
		expect(typeof shoppingList()).toBe('function');
	});
	test('returned function returns shopping list when invoked', () => {
		const testList = shoppingList('potatoes');

		const actual = testList();
		const expected = ['potatoes'];

		expect(actual).toEqual(expected);
	});
	test('returned function - when invoked with an item returns updated list', () => {
		const testList = shoppingList('potatoes');

		const actual = testList('water');
		const expected = ['potatoes', 'water'];

		expect(actual).toEqual(expected);
	});
	test('shoppingList should take any number of arguments', () => {
		const testList = shoppingList('potatoes', 'carrots', 'sprouts');

		const actual = testList();
		const expected = ['potatoes', 'carrots', 'sprouts'];

		expect(actual).toEqual(expected);
	});
});
