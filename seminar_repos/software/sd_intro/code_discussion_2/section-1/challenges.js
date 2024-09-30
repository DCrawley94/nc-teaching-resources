const { check, runTest, skipTest } = require("../test-api/index.js");

// QUESTION 1

function connectStrings() {
  // This function should take 2 strings and join them together with a space in between
  // return this newly created string
}

runTest("connectStrings() can join 2 strings together", function () {
  check(connectStrings("hello", "world")).isEqualTo("hello world");
  check(connectStrings("paul", "rogerson")).isEqualTo("paul rogerson");
  check(connectStrings("blue", "sky")).isEqualTo("blue sky");
});

// QUESTION 2

function checkWordEndsWithIng() {
  // take a string as an argument and return a boolean based on whether the word given ends with 'ing'
}

skipTest(
  "checkWordEndsWithIng() can return true/false for a single word",
  function () {
    check(checkWordEndsWithIng("doing")).isEqualTo(true);
    check(checkWordEndsWithIng("eating")).isEqualTo(true);
    check(checkWordEndsWithIng("bang")).isEqualTo(false);
    check(checkWordEndsWithIng("singer")).isEqualTo(false);
  }
);

// QUESTION 3

function addMissingPunctuation() {
  // take a string as an argument
  // each string may end with a full-stop, exclamation mark, or question mark
  // if the string doesn't end with punctuation, return the string with a full-stop added at the end. Otherwise, return the string unchanged
}

skipTest(
  "addMissingPunctuation() returns the string with accurate punctuation",
  function () {
    check(addMissingPunctuation("Hello there!")).isEqualTo("Hello there!");
    check(addMissingPunctuation("How's it going?")).isEqualTo(
      "How's it going?"
    );
    check(addMissingPunctuation("Yeah I'm good")).isEqualTo("Yeah I'm good.");
    check(addMissingPunctuation("Nice.")).isEqualTo("Nice.");
  }
);

// QUESTION 4

function getRemainder() {
  // This function should take two arguments a and b, and return the remainder of the division of a / b
}

skipTest("getRemainder() returns the correct remainder", function () {
  check(getRemainder(10, 2)).isEqualTo(0);
  check(getRemainder(119, 10)).isEqualTo(9);
  check(getRemainder(50, 6)).isEqualTo(2);
});

// QUESTION 5

function accessObject(obj, key) {
  // This function should take an object and a key as its arguments and return the value found at the provided key in the input object
  // If the key doesn't exist on the object, this function should return a string of "property not found"
}

skipTest("accessObject() can access a property value using a key", function () {
  check(accessObject({ name: "jonny", age: 32 }, "name")).isEqualTo("jonny");
  check(accessObject({ name: "jonny", age: 32 }, "age")).isEqualTo(32);
  check(accessObject({ name: "jonny", age: 32 }, "email")).isEqualTo(
    "property not found"
  );
});

// QUESTION 6

function makeAllWordsBold(arr) {
  // In markdown files (e.g. 'README.md') we can denote words as bold by putting two asterisks on either side of them, such as: **hello**
  // This function should take an array of strings as an argument and return an array consisting of the same strings but in bold - ie with two asterisks either side of them
}

skipTest(
  "makeAllWordsBold() can convert all strings to be surrounded by double asterisks",
  function () {
    check(makeAllWordsBold(["hello", "there", "world"])).isEqualTo([
      "**hello**",
      "**there**",
      "**world**"
    ]);
    check(makeAllWordsBold(["I", "love", "coding"])).isEqualTo([
      "**I**",
      "**love**",
      "**coding**"
    ]);
  }
);

// QUESTION 7

function getPositiveNumbers(arr) {
  // This function should take an array of numbers as an argument and return an array containing all positive numbers from the input (retaining the order)
}

skipTest(
  "getPositiveNumbers() can get all the positive numbers from an array of numbers",
  function () {
    check(getPositiveNumbers([1, -1, 2, -2, 3, -3])).isEqualTo([1, 2, 3]);
    check(getPositiveNumbers([-80, 9, 100, 13, 20, -7])).isEqualTo([
      9, 100, 13, 20
    ]);
    check(getPositiveNumbers([-1, -50, -999])).isEqualTo([]);
  }
);
