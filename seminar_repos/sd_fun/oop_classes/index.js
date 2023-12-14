// ShoppingBasket class:
//   - everything done ✅
// ShoppingBasket class:
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

	addItem(itemName, itemPrice, quantity) {
		const itemDetails = { price: itemPrice, quantity: quantity };
		this.storage[itemName] = itemDetails;
	}

	deleteItem(itemName) {
		delete this.storage[itemName];
	}

	updateItemAmount(itemName, quantity) {
		this.storage[itemName].quantity = quantity;
	}
}

class Customer {
	constructor(name, address) {
		this.name = name;
		this.address = address;
	}

	updateName(newName) {
		this.name = newName;
	}

	updateAddress(newAddress) {
		this.address = newAddress;
	}

	createInvoice() {
		// implement this method
	}
}

module.exports = { ShoppingBasket, Customer };
