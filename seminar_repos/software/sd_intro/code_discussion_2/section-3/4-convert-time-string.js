const { check, runTest, skipTest } = require("../test-api/index.js");

function convertTimeString(string) {
  /*
This function should take a string representing a time with hours and minutes separated by a colon e.g. "13:25"
Some of the times are written in the 24-hour clock format
This function should return the time written in the 12-hour clock format
  */
}

console.log("convertTimeString()");

runTest(
  "returns the string unchanged if already within the right format",
  function () {
    check(convertTimeString("06:28")).isEqualTo("06:28");
  }
);

skipTest("converts an afternoon time to the 12 hour format", function () {
  check(convertTimeString("16:07")).isEqualTo("04:07");
});

skipTest(
  "converts times in the hour after midnight to the 12 hour format",
  function () {
    check(convertTimeString("00:56")).isEqualTo("12:56");
    check(convertTimeString("00:00")).isEqualTo("12:00");
  }
);
