const { check, runTest, skipTest } = require('../test-api/index.js');

// Challenge 10

// This function should take an array as an argument and return an array containing all string elements from the input (retaining the order)

// collectStrings()

function collectStrings(arr) {

  stringArray = [];
  count = 0;

  while (count < arr.length) {

    if(typeof arr[count] === 'string') {
      stringArray.push(arr[count]);
    }
    
    count++
  }

  return stringArray;
}

runTest('collectStrings() can get all the strings from an array', function () {
	check(collectStrings(['a', 'b', 'c'])).isEqualTo(['a', 'b', 'c']);
	check(collectStrings(['a', 10, 'b', 1000, 'c'])).isEqualTo(['a', 'b', 'c']);
});

/******* Refactor Bonus Challenge *******

1. Challenge 5 - complete this problem without resorting to if statements!
2. Refactor every function into an ES6 arrow function () => {}
*/
