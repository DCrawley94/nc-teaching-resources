const { check, runTest, skipTest } = require("../test-api/index.js");

// For this function take a look at what is expected in the tests to help you determine what behaviour your function should exhibit

// declare validMobileNumber here

console.log("validMobileNumber");
runTest("returns false when passed a string of the wrong length", function () {
  check(validMobileNumber("123")).isEqualTo(false);
  check(validMobileNumber("0750617250638")).isEqualTo(false);
  check(validMobileNumber("+447712368768724988")).isEqualTo(false);
});
skipTest("returns true when passed a valid plain phone num string", function () {
  check(validMobileNumber("07506172506")).isEqualTo(true);
});
skipTest("returns true when passed a valid string with a + prefix", function () {
  check(validMobileNumber("+447506172506")).isEqualTo(true);
});
skipTest("returns true when passed a valid international phone num", function () {
  check(validMobileNumber("00447506172506")).isEqualTo(true);
});
skipTest("returns false when passed a string with invalid chars", function () {
  check(validMobileNumber("07506189foo")).isEqualTo(false);
});
skipTest("returns true when passed random other valid phone numbers", function () {
  check(validMobileNumber("00447555123456")).isEqualTo(true);
  check(validMobileNumber("+447676111222")).isEqualTo(true);
  check(validMobileNumber("07898888643")).isEqualTo(true);
  check(validMobileNumber("07766555432")).isEqualTo(true);
  check(validMobileNumber("07989765490")).isEqualTo(true);
});
skipTest("returns false when passed random other invalid phone numbers", function () {
  check(validMobileNumber("004475551&&&23456")).isEqualTo(false);
  check(validMobileNumber("-447676111222")).isEqualTo(false);
  check(validMobileNumber("09898888643")).isEqualTo(false);
  check(validMobileNumber("+449166555432")).isEqualTo(false);
  check(validMobileNumber("00448989765493")).isEqualTo(false);
  check(validMobileNumber("cats")).isEqualTo(false);
});
