const countIceCreams = require('../index');

describe('countIceCreams()', () => {
	test('given array with single item returns 1 if string is iceCream and 0 if not', () => {
		const iceCreamArray = ['iceCream'];
		const notIceCreamArray = ['notIceCream'];
		expect(countIceCreams(iceCreamArray)).toBe(1);
		expect(countIceCreams(notIceCreamArray)).toBe(0);
	});
	test.skip('given array only containing strings will count occurrences of iceCream', () => {
		const someIceCreams = ['iceCream', 'banana', 'iceCream', 'apple'];
		expect(countIceCreams(someIceCreams)).toBe(2);
	});
	test.skip('should count number of iceCreams in nested arrays', () => {
		const nestedIceCream1 = [['iceCream']];
		expect(countIceCreams(nestedIceCream1)).toBe(1);

		const nestedIceCream2 = [[['iceCream']]];
		expect(countIceCreams(nestedIceCream2)).toBe(1);

		const arbitrarilyNestedIceCreams = [
			['iceCream'],
			'sadness',
			[['iceCream'], 'sadness'],
			[[['iceCream', 'sadness'], 'iceCream']]
		];
		expect(countIceCreams(arbitrarilyNestedIceCreams)).toBe(4);
	});
});
