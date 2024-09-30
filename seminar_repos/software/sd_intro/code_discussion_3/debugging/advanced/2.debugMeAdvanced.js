const { check, runTest, skipTest } = require("../../test-api/index.js");

function compoundInterest(value, interestRate, years) {
  let bankAccount = value;
  for (let i = 1; i <= years.length; i++) {
    bankAccount *= interestRate + 1;
  }
  return value;
}

runTest(
  "Returns the same value when interest is zero for 5 years ",
  function () {
    check(compoundInterest(100, 0, 5)).isEqualTo(100);
  }
);
runTest("Returns the same value when years are 0", function () {
  check(compoundInterest(100, 0.1, 0)).isEqualTo(100);
});
runTest(
  "Returns the correct value when interest rates and years > 0",
  function () {
    check(compoundInterest(100, 0.1, 5)).isEqualTo(161.05);
  }
);
