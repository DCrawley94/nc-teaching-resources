# Composite Classes

## **Questions for Jim/Liam:**

"Understand the need composite classes fill within a wider application":

- When wanting to separate concerns - e.g. customer and shopping trolley are two separate things and should not be one class
- similar to extracting functionality from a larger function - things that aren't related to the function or things that want to be re-using

"Know how to identify when to use a composite class":

- When describing a has-a relationship (id the thing in question is relatively complex - not a single attribute for example)
- Stuff on Classes that isn't necessarily related to the class

"Explore why we rely on abstractions (classes) and not implementations (instances)":

- Pokemon Trainer accepts Pokeball constructor: belt is the created a array of 6 contructor invos

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

## Intro

Start with showing current customer class outline on Figjam and ask students if they think there's anything wrong with the class or if there's something they could improve.

Hopefully they give some of these answers but if not tell them directly and explain it:

- The Customer class is trying to do too much
- The ShoppingCart functionality is not related to the Customer functionality
- We can improve it by extracting certain behaviour into a new class and then have the Customer use this new class - explain that this is a concept that will hopefully start to make more sense.

**Relate this to the ides of extracting functionality in JS functions - they should be aware of this**

We extract functionality that is:

- Not tied to the function in question
- Something we want to make re-usable

---

Move down to two code blocks - one with all the Customer functionality and one with an empty ShoppingCart class

**pick students to choose certain behaviours to extract**

| Customer        | ShoppingCart | ###  | Customer        | ShoppingCart |
| --------------- | ------------ | ---- | --------------- | ------------ |
| name: string    |              |      | name: string    | cart: object |
| address: string |              |      | address: string | addItem()    |
| cart: object    |              |      | updateName()    | deleteItem() |
| updateName()    |              | GOES | updateAddress() |              |
| updateAddress() |              | TO   | createInvoice() |              |
| addItem()       |              | ---> |
| deleteItem()    |              |      |
| createInvoice() |              |      |

---

Have part of the class created - focus on testing that the customer has an instance of shoppingCart & the createInvoice method uses `this.cart`
