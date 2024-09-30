const { check, runTest, skipTest } = require("../test-api/index.js");

function validTriangles(triangles) {
  /*
This function that takes an array of triangles.
Each triangle is represented as an array e.g. [10, 12, 22] where the three numbers are the sides of the triangle.
The function should return the count of triangles that are valid.
To be a valid triangle, the sum of any two sides must be larger than the remaining side
  */
}

console.log("validTriangles()");
runTest("returns 0 when passed no triangles []", function () {
  check(validTriangles([])).isEqualTo(0);
});

skipTest("returns 0 when passed an array with no valid triangles", function () {
  check(validTriangles([[5, 10, 25]])).isEqualTo(0);
});

skipTest(
  "returns 1 when passed an array with a single valid triangle",
  function () {
    check(validTriangles([[5, 4, 5]])).isEqualTo(1);
  }
);

skipTest(
  "returns 2 when passed an array with 2 valid and 1 invalid triangle",
  function () {
    check(
      validTriangles([
        [5, 10, 25],
        [5, 4, 5],
        [542, 586, 419]
      ])
    ).isEqualTo(2);
  }
);
