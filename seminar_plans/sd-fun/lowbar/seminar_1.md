# Mock Functions

FIGJAM: https://www.figma.com/file/5DouHJNjTZ2HPWJt9S8QhU/Jest-Mocks?type=whiteboard&node-id=1%3A22&t=8UPvb1B7B6gUPtkM-1

## Learning Objectives:

- Develop the understanding of the students as to when we must use mock functions
- Showcase the benefits of using mock functions to be able to more clearly define the behaviours under test
- Showcase how we can use mock functions to also better represent the behaviours under test in the test implementation

## Refresher: What is a Higher Order Function?

> Pick a student to define a HOF

- Function that takes a function as an argument
- Function that returns a function
- Or both of the above!

## Introduce Problem: (5min)

`copyArrayAndDoSomething`

- takes an array and a function as it's arguments
- will invoke the provided function, with each of the elements of the array
- the output of those invocations will be added to a new array which is returned from the function

**Point out that this might sound familiar to a method they already know - for demonstration purposes we will not be using that method today**

### Introduce the tests: (5min)

**This is not an example of good TDD, this is purely for teaching purposes**

### Solve the problem with the help of the students (20min)

Remove `test.skip` for one test at a time and have students help solve it

**When we ove onto test for reference and mutation, ask students if they think the tests will pass straight away or not - WHY?**
