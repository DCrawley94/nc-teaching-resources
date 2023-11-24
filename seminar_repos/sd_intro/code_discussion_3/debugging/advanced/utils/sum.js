function sumArray(array) {
  array.reduce((accumulator, currentValue) => {
    return accumulator + currentValue;
  }, 1);
}

module.exports = { sumArray };
