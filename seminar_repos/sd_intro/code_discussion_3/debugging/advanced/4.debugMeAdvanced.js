const { check, runTest, skipTest } = require("../../test-api/index.js");
const { sumArray } = require("./utils/sum");

function sumSentence(arr) {
  const costs = arr.map((fruitObj) => fruitObj.cost);
  const total = sumArray(costs);
  return `The total cost of the fruits is £${total}`;
}

runTest("Returns correct string for no fruits", function () {
  check(sumSentence([])).isEqualTo("The total cost of the fruits is £0");
});
runTest("Returns correct string for one fruit", function () {
  check(sumSentence([{ fruit: "apple", cost: 5 }])).isEqualTo(
    "The total cost of the fruits is £5"
  );
});
runTest("Returns correct string for two fruits", function () {
  check(
    sumSentence([
      { fruit: "apple", cost: 5 },
      { fruit: "orange", cost: 4 },
    ])
  ).isEqualTo("The total cost of the fruits is £9");
});
runTest("Returns correct string for many fruits", function () {
  check(
    sumSentence([
      { fruit: "red apple", cost: 5 },
      { fruit: "poison apple", cost: 20 },
      { fruit: "kiwi", cost: 1 },
      { fruit: "tomato ;)", cost: 2 },
      { fruit: "green apple", cost: 5 },
    ])
  ).isEqualTo("The total cost of the fruits is £33");
});
