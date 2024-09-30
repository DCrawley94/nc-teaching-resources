const { check, runTest, skipTest } = require("../test-api/index.js");

/*
This function folds an array in the middle n number of times.

If the list has a odd length, then fold on the middle index (the middle number therefore won't change)
other wise you fold in the 'gap' between the two middle integers and so all integers are folded.

To 'fold' the numbers add them together.

For example:

Fold 1-times:
[1,2,3,4,5] -> [6,6,3]
Here we fold the 1st with the last and the second with the 4th. As it is odd in length, the middle index is not folded
*/
function foldArray() {}

console.log("foldArray");

runTest("folds a even length array", function () {
  check(foldArray([1, 2], 1)).isEqualTo([3]);
  check(foldArray([1, 2, 3, 10, 34, 100], 1)).isEqualTo([101, 36, 13]);
});

skipTest("folds an odd length array", function () {
  check(foldArray([1, 2, 3], 1)).isEqualTo([4, 2]);
});

skipTest("folds an even length array multiple times", function () {
  check(foldArray([1, 2, 3, 10, 34, 100], 2)).isEqualTo([114, 36]);
});

skipTest("folds an array to a single value", function () {
  check(foldArray([1, 2, 3, 10, 34, 100], 3)).isEqualTo([150]);
});

skipTest("repeated folds remain the same", function () {
  check(foldArray([1, 2, 3, 10, 34, 100], 4)).isEqualTo([150]);
});
