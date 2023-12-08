/*
 - function will take an array and a function as it's arguments

 - function will invoke the provided function, with each of the elements of the array 

 - the output of those invocations will be added to a new array
 */
function copyArrayAndDoSomething(array, func) {
	const results = [];

	for (let i = 0; i < array.length; i++) {
		results.push(func(array[i]));
	}

	return results;
}

module.exports = copyArrayAndDoSomething;
