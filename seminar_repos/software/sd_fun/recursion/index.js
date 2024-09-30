function countIceCreams(arr) {
	let count = 0;

	for (let i = 0; i < arr.length; i++) {
		if (arr[i] === 'iceCream') {
			count++;
		} else if (Array.isArray(arr[i])) {
			count += countIceCreams(arr[i]);
		}
	}

	return count;
}

module.exports = countIceCreams;
