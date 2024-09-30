const { check, runTest, skipTest } = require("../test-api/index.js");

function findMissingLetter(letters) {
  /*
In this function, you need to find out which letter is missing. But you can't use a reference lookup table (i.e. no array or object with the whole alphabet in it) so you will have think outside the box!

This function needs to take a list and needs to return the letter it is missing.

You will always get a sorted array of consecutive letters, and it will always have exactly one letter missing. The length of the array will always be at least 2. The array will always contain letters in only one case.
  */
}

console.log("findMissingLetter()");

runTest("returns an empty string if no letters are missing", function () {
  check(findMissingLetter(["A", "B", "C", "D", "E"])).isEqualTo("");
});

skipTest("returns a missing capital letter", function () {
  check(findMissingLetter(["A", "B", "C", "E"])).isEqualTo("D");
});

skipTest("returns a missing lower case letter", function () {
  check(findMissingLetter(["e", "f", "g", "i"])).isEqualTo("h");
});
