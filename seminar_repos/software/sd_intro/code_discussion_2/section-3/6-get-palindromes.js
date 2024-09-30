const { check, runTest, skipTest } = require("../test-api/index.js");

/*
  This function takes an array of words and returns an array containing only the palindromes.
  A palindrome is a word that is spelled the same way backwards.
  E.g. ['foo', 'racecar', 'pineapple', 'porcupine', 'tacocat'] =>  ['racecar', 'tacocat']
*/
function getPalindromes(words) {}

console.log("getPalindromes()");

runTest("returns [] when passed []", function () {
  check(getPalindromes([])).isEqualTo([]);
});

skipTest("identifies palindromes", function () {
  check(getPalindromes(["racecar"])).isEqualTo(["racecar"]);
  check(getPalindromes(["racecar", "racecar"])).isEqualTo([
    "racecar",
    "racecar"
  ]);
});

skipTest("ignores non-palindromes", function () {
  check(getPalindromes(["racecar", "kayak", "tacocat"])).isEqualTo([
    "racecar",
    "kayak",
    "tacocat"
  ]);
  check(getPalindromes(["pineapple", "pony", "racecar"])).isEqualTo([
    "racecar"
  ]);
});

skipTest("returns [] when passed no palindromes", function () {
  check(getPalindromes(["pineapple", "watermelon", "pony"])).isEqualTo([]);
});
