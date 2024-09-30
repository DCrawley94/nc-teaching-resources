const { check, runTest, skipTest } = require("../test-api/index.js");

function alphabetReplace(string) {
  /*
This function that accepts a string of any length, and replaces each letter within each word with the corresponding index that that letter has in the alphabet.

You must have a space between each index number, and do NOT need to account extra for spaces between words.
  */
}

console.log("alphabetReplace()");

runTest("replaces the letters in a single word with codes", function () {
  check(alphabetReplace("code")).isEqualTo("3 15 4 5");
});

skipTest("is case-insensitive", function () {
  check(alphabetReplace("Northcoders")).isEqualTo(
    "14 15 18 20 8 3 15 4 5 18 19"
  );
});

skipTest("ignores spaces between words", function () {
  check(alphabetReplace("expert programming")).isEqualTo(
    "5 24 16 5 18 20 16 18 15 7 18 1 13 13 9 14 7"
  );
});
