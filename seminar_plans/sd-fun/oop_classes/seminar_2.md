# Composite Classes

## Learning Objectives

- To understand what composite classes are
- To understand the need for composite classes

**If students have reached part 5/6 then this will be relevant**

## Intro

Start with showing current customer class outline on Figjam and ask students if they think there's anything wrong with the class or if there's something they could improve.

**Hopefully they give some of these answers but if not tell them directly and explain it:**

- The Customer class has too many responsibilities
- It has to manage the Customer data/methods and also Shopping Cart data/methods
- The ShoppingCart functionality is not related to the Customer functionality

**Ask for ideas on what we can do differently:**

- We can improve it by extracting certain behaviour into a new class and then have the Customer use this new class

**Dive into why we would want to do this:**

- Modularity: You can break down complex systems into smaller, more manageable parts. Each part (class) can be developed, tested, and modified independently - **this is very similar to the reasoning of why we might want to extract certain behaviours from a function and break it down into smaller chunks.**

- Reusability: Other parts of the program might want to make use of the new Class - **this means we wouldn't need to re-write the same code and DRY things up**

- Encapsulation: Each class is responsible for its own functionality. This promotes encapsulation, a key OOP principle, by keeping the implementation details of each class hidden from the others.

**explain that this is a concept that will hopefully start to make more sense**

---

Move down to two code blocks which will be showing new structure.

**Highlight how the code needed for the ShoppingCart functionality has been extracted into another class**

**Point out that we can attach an instance of the ShoppingCart to the Customer class**

🤯 The customer is now what's known as a **composite class** 🤯

Usefulness:

- When wanting to separate concerns - e.g. customer and shopping trolley are two separate things and should not be one class
- similar to extracting functionality from a larger function - things that aren't related to the function or things that want to be re-using

"Know how to identify when to use a composite class":

- if you think something would benefit from being extracted.

## TDD Time

Switch to VSCode with pre-made ShoppingCart class and part-built Customer class

Show the students what has been created so far:

- ShoppingCart class

  - cart
  - addItem()
  - deleteItem()
  - updateItemAmount()

- Customer class
  - name
  - address
  - updateName()
  - updateAddress()

---

**Ask students to suggest some possible behaviours we could test for**

> Note these down in pseudocode and organise them in a logical order

- Customer should have a cart property that is an instance of ShoppingCart

> Use jest .toBeInstanceOf matcher

**To Do**:

- cart attribute on the cart:
  - Test that testCustomer.cart is **an instance of** ShoppingCart
- createInvoice()
  - assume happy path - single item, , quantity 1
    - returns object like this:
    ```js
    {
      name: 'customer name',
      address: 'customer address',
      orderDetails: {
        item1: {
          price: 10,
          quantity: 1
        },
        item2: {
          price: 20,
          quantity: 2
        }
      },
      total: // number: total cost
    }
    ```
  - multiple items, quantity 1
  - single item, quantity > 1
  - multiple items, quantity > 1

**if there is time**:

- cart
  - Test that it's only added when it's the correct type of instance? why do we need this?

---

## **Questions for Jim/Liam:**

"Understand the need composite classes fill within a wider application":

- When wanting to separate concerns - e.g. customer and shopping trolley are two separate things and should not be one class
- similar to extracting functionality from a larger function - things that aren't related to the function or things that want to be re-using

"Know how to identify when to use a composite class":

- When describing a has-a relationship (id the thing in question is relatively complex - not a single attribute for example)
- Stuff on Classes that isn't necessarily related to the class

"Explore why we rely on abstractions (classes) and not implementations (instances)":

- Pokemon Trainer accepts Pokeball constructor: belt is the created a array of 6 constructor invos

"Highlight what is an abstraction (a class) and what is an instance, or an implementation, and why we would like to rely on a ShoppingBasket class, and not on an individual shopping basket instance in the composite Customer class."

- ❓❓❓❓❓❓ I don't know what this means ❓❓❓❓❓❓ - the Customer class contains an instance of a Shopping cat, not the whole class?

Ask Vel if I should pass class or instances to customer constructor\*\*
**Are the classes in the example enough or should we use more?**

- createReceipt() method on customer to use shopping cart

### ✨Vocab I don't know✨:

- Base class: **The class that is inherited from**
- Derived class: **The class that inherits**
- abstraction(class)
- concretion (instance)

## Composition Analogy:

The relationships that are described by composition are not the same as relationships described by inheritance.

|              | Inheritance        | Composition                    |
| ------------ | ------------------ | ------------------------------ |
| Relationship | "is a"             | "has a"                        |
| Example      | a pug **is a** dog | a car **has a** steering wheel |
|              |                    |                                |
|              |                    |                                |

## Why use composite classes?

Modularity: You can break down complex systems into smaller, more manageable parts. Each part (class) can be developed, tested, and modified independently.

Reusability: If you have other objects in your program that also need a processor, memory, or hard drive, you can reuse the Processor, Memory, and HardDrive classes rather than rewriting the same code.

Encapsulation: Each class is responsible for its own functionality. This promotes encapsulation, a key OOP principle, by keeping the implementation details of each class hidden from the others.

In summary, composite classes in OOP allow you to model complex systems by combining simpler classes, making your code more modular, reusable, and organized.

## General Plan:

Have part of the class created - focus on testing that the customer has an instance of shoppingCart & the createInvoice method uses `this.cart`
