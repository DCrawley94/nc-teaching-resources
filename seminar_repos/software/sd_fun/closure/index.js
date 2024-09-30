function shoppingList(...items) {
	const newList = [...items];

	function innerFunc(newItem) {
		// add new item to shopping list
		if (newItem) {
			newList.push(newItem);
		}

		return newList;
	}
	return innerFunc;
}

module.exports = shoppingList;
