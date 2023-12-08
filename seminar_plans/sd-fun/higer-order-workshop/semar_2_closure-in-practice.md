# Closure in Practice

## Learning Objectives

- Be able to solve a problem that requires Closure
- Use TDD to solve a problem that involves Closure

## Introduce Problem

Function: `shoppingList`

Function should accept any number of items to go on a shopping list and return a function that allows us to add items to that shopping list.

The returned function should be able to accept a string that represents the item being added.

The returned function should return the updated array containing the shopping list items:

```js
const christmasShopping = shoppingList('chicken', 'potatoes');

christmasShopping();
// Returns ['chicken','potatoes']

christmasShopping('sprouts');
// Returns ['chicken','potatoes', 'sprouts']

christmasShopping('stuffing');
// Returns ['chicken','potatoes', 'sprouts', 'stuffing']
```

✨🎅✨*festive*✨🎅✨

## TDD/Solution

Discuss test for basic behaviours:

Ask students for suggestions for the first test.

### Test for returning function

**Highlight that on first invocation the a function is returned**

> NIce simple solution - pick a student for answer

```js
test('shoppingList should return a function', () => {
	const testList = shoppingList();

	expect(typeof testList).toBe('function');
});
```

```js
function shoppingList() {
	function innerFunc() {}
	return innerFunc;
}
```

### Returned function returns array with single item in list

> Build up test complexity - save function to variable before invoking.

**Can also use this to show double invocation like students will have seen in tests** - `shoppingList('milk')()` - don't use this properly though as it looks super confusing.

```js
test('', () => {
	const testList = shoppingList('milk');

	const expected = ['milk'];
	const actual = testList();

	expect(actual).toEqual(expected);
});
```

Ask for solutions to this part - make references to:

- original function is garbage collected
- array being stored in the COVE
- **A closure is created when the inner function is created - this happens when the shoppingList function is executed**
- The Inner function is still able to use the array because it was in scope when the function was created.

```js
function shoppingList(item) {
	const list = [item];
	function innerFunc() {
		return list;
	}
	return innerFunc;
}
```

---

A bit of an abstract explanation:

```txt
Closures are useful because they let you associate data (the lexical environment) with a function that operates on that data.
```

### Returned function returns array with multiple items in list

```js
test('', () => {
	const testList = shoppingList('milk', 'eggs');

	const expected = ['milk', 'eggs'];
	const actual = testList();

	expect(actual).toEqual(expected);
});
```

Ask students if anyone has come across a way of handling unknown numbers of arguments.

If no-one mentions **rest** operator then can lead them to it.

Regardless go into the docs: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters

Can also show the differences with **spread**:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax

```js
function shoppingList(...items) {
	const list = [...items];
	function innerFunc() {
		return list;
	}
	return innerFunc;
}
```

### Returned function can add new items to the list

```js
test('', () => {
	const testList = shoppingList('milk', 'eggs');

	const expected = ['milk', 'eggs', 'carrots'];
	const actual = testList('carrots');

	expect(actual).toEqual(expected);
});
```

```js
function shoppingList(...items) {
	const list = [...items];
	function innerFunc(newItem) {
		if (items !== undefined) {
			list.push(newItem);
		}
		return list;
	}
	return innerFunc;
}
```

---

**Round down session - point out how we've made use of a closure to keep hold of the `list` variable**
