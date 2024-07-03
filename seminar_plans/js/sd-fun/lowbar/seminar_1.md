# Mock Functions

FIGJAM: https://www.figma.com/file/5DouHJNjTZ2HPWJt9S8QhU/Jest-Mocks?type=whiteboard&node-id=1%3A22&t=8UPvb1B7B6gUPtkM-1

## Learning Objectives:

- Develop the understanding of the students as to when we must use mock functions
- Showcase the benefits of using mock functions to be able to more clearly define the behaviours under test
- Showcase how we can use mock functions to also better represent the behaviours under test in the test implementation

## Refresher: What is a Higher Order Function?

> Pick a student to define a HOF

- Function that takes a function as an argument
- Function that returns a function
- Or both of the above!

## Introduce Problem: (5min)

`copyArrayAndDoSomething`

- takes an array and a function as it's arguments
- will invoke the provided function, with each of the elements of the array
- the output of those invocations will be added to a new array which is returned from the function

**Point out that this might sound familiar to a method they already know - for demonstration purposes we will not be using that method today**

### Introduce the tests: (5min)

**This is not an example of good TDD, this is purely for teaching purposes**

### Solve the problem with the help of the students (20min)

Remove `test.skip` for one test at a time and have students help solve it

**When we move onto test for reference and mutation, ask students if they think the tests will pass straight away or not - WHY?**

- can force the tests to fail but also can gloss over it instead. The code we've written so far already meets the requirements but it's still a good idea to double check

## Discussion about the tests

Questions:

- Are the tests actually testing the behaviour of the function `copyArrayAndDoSomething`
- What are the behaviours of the function we're writing?
  - not tied to the passed in function
  - function should be invoked once per array element
  - function should take single argument > each array element in turn
  - output of function should be added to new array > this behaviour is currently covered by the tests but we will look into this more

## How can we isolate this behaviour and test it?

Throw back to the lecture and being shown how to create a Mock object for testing.

We could create our own Mock like so:

```js
let invoCount = 0;

function mock() {
	invoCount += 1;
}

copyArrayAndDoStuff([1, 2, 3, 4, 5], mock);

expect(invoCount).toBe(5);
```

This would allow us to check how many times the passed function was invoked

We could also have something like this:

```js
let passedArgs = [];

function mock(element) {
	passedArgs.push(element);
}

copyArrayAndDoStuff([1, 2, 3, 4, 5], mock);

expect(passedArgs).toEqual([1, 2, 3, 4, 5]);
```

This would allow us to check the arguments given to the `copyArrayAndDoStuff` function.

**HOWEVER...**
✨*There is an easier way*✨

We can use Jest Mocks 🤯 😮

## Jest Mocks:

Show documentation: https://jestjs.io/docs/mock-functions

Point out the example testing a `forEach`.

Don't focus on the code, focus on what is being tested:

- number of calls
- passed arguments

**This sounds useful!**

### `.mock` property

https://jestjs.io/docs/mock-functions#mock-property

This contains data about how the Mock function has been used.

**Secret Shopper Analogy**

- Keeps notes on how it has been treated (call count, arguments) and creates a report (`.mock` property).

### Useful Matchers

**Bit awkward navigating the `.mock` information as it's a large object.**

**Luckily there are some handy dandy matchers**

https://jestjs.io/docs/mock-functions#custom-matchers

Full list of Jest matchers: https://jestjs.io/docs/expect

## Tests with `Jest.fn`

### Test One: Function called certain number of times

```js
test('function invokes provided function required number of times', () => {
	const mockFunc = jest.fn();
	const input = [1, 2, 3, 4];

	copyArrAndDoSomething(input, mockFunc);

	expect(mockFunc).toHaveBeenCalledTimes(4);
});
```

### Test Two: function is invoked with correct arguments

```js
test('function invokes provided function with expected values', () => {
	const mockFunc = jest.fn();
	const input = [1, 2, 3, 4];

	copyArrayAndDoSomething(input, mockFunc);

	expect(mockFunc).toHaveBeenCalledWith(1);
	expect(mockFunc).toHaveBeenCalledWith(2);
	expect(mockFunc).toHaveBeenCalledWith(3);
	expect(mockFunc).toHaveBeenCalledWith(4);
});
```

### Test 3: Output of Given Function is added to new array

Documentation on this: https://jestjs.io/docs/mock-functions#mock-return-values

```js
test('provided function returns expected value on each invocation', () => {
	const mockFunc = jest.fn((n) => {
		return n + 2;
	});
	mockFunc.mockReturnValue = 10;

	const actualOutput = copyArrayAndDoSomething([1, 2, 3], mockFunc);
	const expectedOutput = [10, 10, 10];

	expect(actualOutput).toEqual(expectedOutput);
});
```

**Can also show this as an option**

```js
const mockFunc = jest.fn((n) => {
	return n + 2;
});
```

### Finish Off

Ask which set of tests are more clear about the behaviour they're testing.

> Students hopefully choose the mock ones

- The mock tests focus on the behaviour of `copyArrAndDoSomething` rather than the behaviours of the passed in function
- the passed function could do anything really.
- The key behaviour is how the passed function is invoked and what is done with the return value.

**Point out that this isn't a particularly realistic use case for mocking, this is just a demonstration of how to use Jest Mocks**

Round off by talking about how mocking is very useful for testing as it allows us to control things that are usually out of our control - e.g. things that are random, other function calls that are slowing tests down.
