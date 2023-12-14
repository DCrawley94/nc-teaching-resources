const { ShoppingBasket, Customer } = require('../index');

describe('ShoppingBasket', () => {
	test('storage property should default to an empty object', () => {
		const testShoppingBasket = new ShoppingBasket();
		expect(testShoppingBasket.storage).toEqual({});
	});
	test('addItem should add an item details object to the storage object with the correct key', () => {
		const testShoppingBasket = new ShoppingBasket();

		testShoppingBasket.addItem('testItem', 10, 5);

		const expectedStorage = { testItem: { price: 10, quantity: 5 } };

		expect(testShoppingBasket.storage).toEqual(expectedStorage);
	});
	test('deleteItem should remove specified item from the storage object', () => {
		const testShoppingBasket = new ShoppingBasket();

		testShoppingBasket.addItem('testItem', 10, 5);
		testShoppingBasket.deleteItem('testItem');

		expect(testShoppingBasket.storage).toEqual({});
	});
	test('updateItemAmount should update a given items quantity', () => {
		const testShoppingBasket = new ShoppingBasket();

		testShoppingBasket.addItem('testItem', 10, 5);
		testShoppingBasket.updateItemAmount('testItem', 10);

		const expectedStorage = { testItem: { price: 10, quantity: 10 } };
		expect(testShoppingBasket.storage).toEqual(expectedStorage);
	});
});

describe('Customer', () => {
	test('instance should have a name property', () => {
		const testCustomer = new Customer('geoff');

		expect(testCustomer.name).toBe('geoff');
	});
	test('instance should have an address property', () => {
		const testCustomer = new Customer(
			'geoff',
			'742 Evergreen Terrace, Springfield'
		);

		expect(testCustomer.address).toBe('742 Evergreen Terrace, Springfield');
	});
	test('updateName method should change customer name', () => {
		const testCustomer = new Customer(
			'geoff',
			'742 Evergreen Terrace, Springfield'
		);

		testCustomer.updateName('Homer Simpson');

		expect(testCustomer.name).toBe('Homer Simpson');
	});
	test('updateAddress method should change customer address', () => {
		const testCustomer = new Customer('Homer Simpson', 'somewhere');

		testCustomer.updateAddress('742 Evergreen Terrace, Springfield');

		expect(testCustomer.address).toBe('742 Evergreen Terrace, Springfield');
	});
});
