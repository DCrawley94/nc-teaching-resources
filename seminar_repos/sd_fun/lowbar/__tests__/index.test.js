const copyArrayAndDoSomething = require('../index');

describe.skip('copyArrayAndDoSomething', () => {
	test('if passed an empty numbers array, function will return an empty array', () => {
		const input = [];
		const add3 = (n) => {
			return n + 3;
		};

		expect(copyArrayAndDoSomething(input, add3)).toEqual([]);
	});
	test('will implement the provided functions behaviour on an array containing a single value', () => {
		const input = [3];
		const multiplyBy4 = (n) => {
			return n * 4;
		};

		expect(copyArrayAndDoSomething(input, multiplyBy4)).toEqual([12]);
	});
	test('will implement the provided functions behaviour on an array of values', () => {
		const input = ['August', 'Chon', 'Simon', 'Mick'];
		const greetMentor = (mentor) => {
			return `Hello ${mentor}!`;
		};

		expect(copyArrayAndDoSomething(input, greetMentor)).toEqual([
			'Hello August!',
			'Hello Chon!',
			'Hello Simon!',
			'Hello Mick!'
		]);
	});
	test('function does not mutate original array input', () => {
		const input = [1];
		const add3 = (n) => {
			return n + 3;
		};

		copyArrayAndDoSomething(input, add3);
		expect(input).toEqual([1]);
	});
	test('function returns a new object in memory', () => {
		const input = [3];
		const multiplyBy4 = (n) => {
			return n * 4;
		};

		expect(copyArrayAndDoSomething(input, multiplyBy4)).not.toBe(input);
	});
});

describe('copyArrayAndDoSomething - Mock Tests', () => {
	test('passed in function is invoked the correct number of times', () => {
		const mockFunc = jest.fn();
		const input = [1, 2, 3, 4, 5];

		copyArrayAndDoSomething(input, mockFunc);

		expect(mockFunc).toHaveBeenCalledTimes(5);
	});
	test('passed in function is invoked with the correct arguments', () => {
		const mockFunc = jest.fn();
		const input = ['a', 'b', 'c'];

		copyArrayAndDoSomething(input, mockFunc);

		expect(mockFunc).toHaveBeenCalledWith('a');
		expect(mockFunc).toHaveBeenCalledWith('b');
		expect(mockFunc).toHaveBeenCalledWith('c');
	});
});
