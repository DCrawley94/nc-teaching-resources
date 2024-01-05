# Recap of Pure Functions and Testing for Mutation/Reference

## Intro

Ask students to tell me what a pure function is and write down on sticky notes.

Key Points:

- Always returns the same result given certain arguments: this is handled by our usual tests
- No observable side effects:
  - Does not mutate data
  - There are other possible side effects

## Recap on Value vs Reference

As we know functions, arrays and objects are non-primitive data types and as such when variables are assigned they are assigned a reference to an object

## What does this mean in relation to testing

How can we test for mutation?

```txt

input > fn() > output

```

Does the input still look the same after the function has been invoked?

If the output is the same data type we might also want to make sure that the reference is different!

## Write Tests

```js
test('does not mutate input', () => {
	const testInput = [
		{ name: 'Mick', age: 21, location: 'Liverpool-ish' },
		{ name: 'August', age: 21, location: 'Ancoats' },
		{ name: 'Chon', age: 21, location: 'Somewhere else' }
	];

	moveToManchester(testInput);

	expect(testInput).toEqual([
		{ name: 'Mick', age: 21, location: 'Liverpool-ish' },
		{ name: 'August', age: 21, location: 'Ancoats' },
		{ name: 'Chon', age: 21, location: 'Somewhere else' }
	]);
});

test('output has a different reference in memory', () => {
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
```
