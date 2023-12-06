const copyArrayAndDoSomething = require('../index');

describe('copyArrayAndDoSomething', () => {
	test('if passed an empty numbers array, function will return an empty array', () => {
		const input = [];
		const add3 = (n) => {
			return n + 3;
		};

		expect(copyArrayAndDoSomething(input, add3)).toEqual([]);
	});
	test.skip('will implement the provided functions behaviour on an array containing a single value', () => {
		const input = [3];
		const multiplyBy4 = (n) => {
			return n * 4;
		};

		expect(copyArrayAndDoSomething(input, multiplyBy4)).toEqual([12]);
	});
	test.skip('will implement the provided functions behaviour on an array of values', () => {
		const input = [1, 2, 3, 4];
		const add2andMultiplyBy3 = (n) => {
			return (n + 2) * 3;
		};

		expect(copyArrayAndDoSomething(input, add2andMultiplyBy3)).toEqual([
			9, 12, 15, 18
		]);
	});
	test.skip('function does not mutate original array input', () => {
		const input = [1];
		const add3 = (n) => {
			return n + 3;
		};

		copyArrayAndDoSomething(input, add3);
		expect(input).toEqual([1]);
	});
	test.skip('function returns a new object in memory', () => {
		const input = [3];
		const multiplyBy4 = (n) => {
			return n * 4;
		};

		expect(copyArrayAndDoSomething(input, multiplyBy4)).not.toBe(input);
	});
});
