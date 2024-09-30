// ShoppingBasket class:
//   - everything done ✅
// Customer class:
//   - name  ✅
//   - address ✅
//   - cart
//   - updateName() ✅
//   - updateAddress() ✅
//   - createInvoice()

class ShoppingBasket {
	constructor() {
		this.storage = {};
	}

	addItem(itemName, itemPrice) {
		this.storage[itemName] = itemPrice;
	}

	deleteItem(itemName) {
		delete this.storage[itemName];
	}

	getItems() {
		return Object.keys(this.storage);
	}

	calculateTotalCost() {
		const prices = Object.values(this.storage);

		return prices.reduce((totalPrice, nextPrice) => totalPrice + nextPrice, 0);
	}
}

class Customer {
	constructor(name, address, cart) {
		this.name = name;
		this.address = address;
		this.cart = cart;
	}

	updateName(newName) {
		this.name = newName;
	}

	updateAddress(newAddress) {
		this.address = newAddress;
	}

	createInvoice() {
		// should create invoice object
		// invoiceObject should have customer name, address, list of items, totalCost
		const invoice = {
			name: this.name,
			address: this.address,
			items: this.cart.getItems(),
			totalCost: this.cart.calculateTotalCost()
		};

		return invoice;
	}
}

module.exports = { ShoppingBasket, Customer };
