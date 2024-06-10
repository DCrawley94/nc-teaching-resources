# Pure Functions and Immutability

Introduce the problem on Figjam (link here when made), when talking through it emphasise that the functions returns a **new** dictionary and is a **pure** function.

## TDD

Get students to lead me through TDD, utilise **arrange**/**act**/**assert** for all tests.

Possible build up of tests:

- empty list (only do this if students suggest it) - can discuss benefits of this (if this fails then something has gone very wrong) vs the negatives (is this really testing the happy path/actual behaviour?)
- single profile that's already Python
- single profile non Python
- **At this point push for mutation/reference tests** - at this point it might be good to questions students on the difference between `copy`/`deepcopy`
- multiple profile non Python

Might need to force certain tests to fail
