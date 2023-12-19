const countTheWorlds = require('../countTheWorlds');

jest.setTimeout(1000);

describe('countTheWorlds', () => {
	test('should invoke the callback with null if there is no error', (done) => {
		function testCB(err, data) {
			expect(err).toBe(null);
			done();
		}

		countTheWorlds(testCB);
	});
	test('should invoke the callback with a number', (done) => {
		function testCB(err, data) {
			expect(typeof data).toBe('number');
			done();
		}

		countTheWorlds(testCB);
	});
	test("should invoke the callback with the correct count of 'world' in the text file", (done) => {
		function testCB(err, data) {
			expect(data).toBe(10);
			done();
		}

		countTheWorlds(testCB);
	});
});
