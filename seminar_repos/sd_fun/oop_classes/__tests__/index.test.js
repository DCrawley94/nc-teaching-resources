const { ShoppingBasket, Customer } = require('../index');

describe('ShoppingBasket', () => {
	test('storage property should default to an empty object', () => {
		const testShoppingBasket = new ShoppingBasket();
		expect(testShoppingBasket.storage).toEqual({});
	});

	test('addItem should add an item details object to the storage object with the correct key', () => {
		const testShoppingBasket = new ShoppingBasket();

		testShoppingBasket.addItem('testItem', 10);

		const expectedStorage = { testItem: 10 };

		expect(testShoppingBasket.storage).toEqual(expectedStorage);
	});

	test('deleteItem should remove specified item from the storage object', () => {
		const testShoppingBasket = new ShoppingBasket();

		testShoppingBasket.addItem('testItem', 10);
		testShoppingBasket.deleteItem('testItem');

		expect(testShoppingBasket.storage).toEqual({});
	});

	test('getItems should returns names of all the items in storage', () => {
		const testShoppingBasket = new ShoppingBasket();

		testShoppingBasket.addItem('testItemA', 10);
		testShoppingBasket.addItem('testItemB', 20);

		expect(testShoppingBasket.getItems()).toEqual(['testItemA', 'testItemB']);
	});

	test('calculateTotalCost should return total cost of items in storage', () => {
		const testShoppingBasketA = new ShoppingBasket();
		testShoppingBasketA.addItem('testItemA', 10);

		expect(testShoppingBasketA.calculateTotalCost()).toBe(10);

		const testShoppingBasketB = new ShoppingBasket();
		testShoppingBasketB.addItem('testItemA', 10);
		testShoppingBasketB.addItem('testItemB', 20);

		expect(testShoppingBasketB.calculateTotalCost()).toBe(30);
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
	// cart property test
	test('instance should have a cart property that is an instance of ShoppingCart', () => {
		const newCart = new ShoppingBasket();
		const newCustomer = new Customer('Karl', 'Manchester', newCart);

		expect(newCustomer.hasOwnProperty('cart')).toBe(true);
		expect(newCustomer.cart).toBeInstanceOf(ShoppingBasket);
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
	// createInvoice returns object
	test('createInvoice returns object', () => {
		const testShoppingCart = new ShoppingBasket();
		const testCustomer = new Customer('geoff', 'somewhere', testShoppingCart);

		const output = testCustomer.createInvoice();

		expect(typeof output).toBe('object');
	});
	// return invoice object for cart with single item
	test('createInvoice returns invoice object for a cart with a single item', () => {
		const testShoppingCart = new ShoppingBasket();
		testShoppingCart.addItem('banana', 10);

		const testCustomer = new Customer('Mickey', 'Disneyland', testShoppingCart);

		const output = testCustomer.createInvoice();
		const expectOutput = {
			name: 'Mickey',
			address: 'Disneyland',
			items: ['banana'],
			totalCost: 10
		};

		expect(output).toEqual(expectOutput);
	});
	// return invoice object for cart with multiple items
	test('createInvoice returns invoice object for a cart with multiple items', () => {
		const testShoppingCart = new ShoppingBasket();
		testShoppingCart.addItem('banana', 10);
		testShoppingCart.addItem('cheese', 5);
		testShoppingCart.addItem('gatorade', 50);

		const testCustomer = new Customer('Mickey', 'Disneyland', testShoppingCart);

		const output = testCustomer.createInvoice();
		const expectOutput = {
			name: 'Mickey',
			address: 'Disneyland',
			items: ['banana', 'cheese', 'gatorade'],
			totalCost: 65
		};

		expect(output).toEqual(expectOutput);
	});
});
