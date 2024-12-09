# Testing HOFs - Seminar 2

In this repo you will find a bit of a contrived example tat may be useful for demonstrating the benefits of modular, loosely coupled code that makes use of dependency injection.

## Example 1

In this file is a `process_numbers` function which does some filtering and transforming on the given number list.

Negatives of this approach include:

1. Hard to Understand: (admittedly this contrived example is fairly simple but hopefully students can see how the problems may arise in their code)

   The function does several things (filtering, doubling) all at once. This makes it harder to read and understand at a glance, especially for someone new to the code.

2. Difficult to Maintain:

   If you need to change how one part of the process works (like filtering), you have to dig into the code to make changes. increasing the risk of breaking code and introducing bugs.

3. Limited Reusability:

   The function is tightly coupled to specific tasks (filtering odd numbers, doubling them, and summing). If you want to reuse part of this logic (like just the filtering or doubling), you have to rewrite it elsewhere. **This is not DRY 😱**

4. Harder to test:

   Testing the function is more difficult because it does multiple things at once. If there’s a bug, it’s harder to pinpoint which part of the process is causing the problem.

5. Lack of Flexibility:

   You can't easily change what the function does without modifying its internal logic. For example, if you wanted to filter even numbers instead or apply a different transformation, you would have to rewrite parts of the function.

## Example 2

In this file the `process_numbers` function has been refactored to take a **filtering function** and a **transforming function**.

The benefits of this approach are summarised below:

1. Modularity:

   The refactored version separates the concerns into three distinct utility functions: filter_odd_numbers and double_numbers. This makes each function simpler and easier to understand.

2. Dependency Injection:

   By passing the utility functions as arguments to process_numbers, we achieve loose coupling. The main function doesn't need to know the details of how filtering or transforming is done. It just uses the functions provided to it.

3. Flexibility:

   The refactored function can now be reused with different filtering and transforming functions without any changes to its core logic. This promotes reusability and adaptability to new requirements.

It could even be improved by extracting the `sum` logic, what if we wanted to aggregate the data in a different way?
