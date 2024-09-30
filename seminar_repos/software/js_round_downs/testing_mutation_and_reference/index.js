// Should accept an array of "Person" objects
// {name: "Geoff", age: 21, location: "London"}
// Should update the location property to be "Manchester" and return the array

function moveToManchester(people) {
	const updatedPeople = people.map((person) => {
		const personCopy = { ...person };
		personCopy.location = 'Manchester';
		return personCopy;
	});

	return updatedPeople;
}

module.exports = moveToManchester;
