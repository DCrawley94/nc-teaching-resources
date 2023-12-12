# Recursion

## Learning Objectives

- Understand when Recursion is necessary
- Know the 3 components of a recursive function

## Intro - A Use Case for Recursion

**Nested Data Structures**

A common use case for recursion is for accessing or manipulating nested data structures.

Take a look at the following example:

```js
{
  a: {
    desiredData: "example data"
  },
  b: {
    c: {
      desiredData: "example data"
    }
  },
  d: {
    e: {
      f: {
        g: {
          desiredData: "example data"
        }
      }
    }
  }
}
```

- Let's say I want to access certain data from a nested object
- **But** I don't know how deep the nesting is
- **Recursion can be useful to help me traverse the nested structure and find the information I want**
- This is helpful as while I could use an iterative solution that would likely get very messy with lots of nested loops.

---

**🏁 CHECKPOINT 🏁**

---

## Introduce the Problem:

**countIceCreams**

create a function that accepts an array as an argument, this array will either contain strings or arrays which can also contain strings. The function should count the number of times a string of "iceCream" appears inside these arrays.

```js
countIceCreams(['banana', 'iceCream']); // 1

countIceCreams(['banana', 'iceCream', ['tofu', ['iceCream']], 'iceCream']); // 3
```

**❗ After talking through ask students why we might need recursion here ❗**

---

**🏁 CHECKPOINT 🏁**

---

## Solving the Problem

Before moving to VSCode ask students what they think the base case might be.

> Counting ice creams in a single non-nested array.

### Test 1: Single element array returns 1 or 0

```js
test('given array with single item returns 1 if string is iceCream and 0 if not', () => {
	const iceCreamArray = ['iceCream'];
	const notIceCreamArray = ['notIceCream'];
	expect(countIceCreams(iceCreamArray)).toBe(1);
	expect(countIceCreams(notIceCreamArray)).toBe(0);
});
```

No recursion required:

**ASK STUDENT TO DIRECT ME IN A SOLUTION**

```js
function countIceCreams(arr) {
	let count = 0;
	for (const item of arr) {
		if (item === 'iceCream') count++;
	}
	return count;
}
```

### Test 2: Multi element array returns count of ice creams

```js
test('given array only containing strings will count occurrences of iceCream', () => {
	const someIceCreams = ['iceCream', 'banana', 'iceCream', 'apple'];
	expect(countIceCreams(someIceCreams)).toBe(2);
});
```

**Same solution - force a fail**

```js
function countIceCreams(arr) {
	let count = 0;
	for (const item of arr) {
		if (item === 'iceCream') count++;
	}
	return count;
}
```

### Test 3: Nested Ice Creams

```js
test('should count number of iceCreams in nested arrays', () => {
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
```

Possible Solution:

```js
function countIceCreams(arr) {
	let count = 0;
	for (const item of arr) {
		if (Array.isArray(item)) {
			count += countIceCreams(item);
		} else if (item === 'iceCream') count++;
	}
	return count;
}
```

Highlight the base case:

```js
if (item === 'iceCream')
```

The recursive case:

```js
if (Array.isArray(item))
```

The recursive call:

```js
count += countIceCreams(item);
```

## EC Diagram

Use this input:

```js
[
	['iceCream'],
	'sadness',
	[['iceCream'], 'sadness'],
	[[['iceCream', 'sadness'], 'iceCream']]
];
```

- INITIAL INVO
- arr and count vars declared
- for loop - gloss over item var
- first el: count is reassigned to be current val + result of calling countIceCreams (**SHOW BY LEAVING COUNT WITH NO VALUE FOR NOW**)
  - SECOND CALL
  - arr and count vars declared
  - for loop
  - single element ice cream > count var incremented
  - count returned
- count variable is reassigned to be `1`
- Next el skipped over because no array an no ice cream
- Next el is array: count is reassigned to be current val + result of calling countIceCreams
  - THIRD CALL
  - arr and count vars declared
  - for loop
  - Next el is array: count is reassigned to be current val + result of calling countIceCreams
    - FOURTH CALL
    - arr and count vars declared
    - for loop
    - single element ice cream > count var incremented
    - count returned
  - count variable is reassigned to be `1`
  - Next el skipped over because no array an no ice cream
  - count returned
- count variable is reassigned to be `2`
- Next el is array: count is reassigned to be current val + result of calling countIceCreams
  - FIFTH CALL
  - arr and count vars declared
  - for loop
  - Next el is array: count is reassigned to be current val + result of calling countIceCreams
    - SIXTH CALL
    - arr and count vars declared
    - for loop
    - Next el is array: count is reassigned to be current val + result of calling countIceCreams
      - SEVENTH CALL
      - arr and count vars declared
      - for loop
      - Next el is ice cream
      - count incremented
      - next el is not ice cream - skipped
      - return count
    - count is reassigned to be `1`
    - Next el is ice cream
    - count incremented to `2`
    - return count
  - count is reassigned to be `2`
  - count returned
- count variable is reassigned to be `4`
- count returned
- FINAL OUTPUT IS 4
