# `sum_alphabet_indices`

- This function should take a **string** as argument and return an **integer**
- That integer that is returned will be sum of the index positions of the string characters as they appear in the alphabet (taking into account zero indexing)
- the function will ignore any characters that are not lowercase letters

## Examples:

```py
sum_alphabet_indices("") # --> 0
sum_alphabet_indices("a") # --> 0
sum_alphabet_indices("hello") # --> 7 + 4 + 11 + 11 + 14 = 47
sum_alphabet_indices("Hello") # --> 4 + 11 + 11 + 14 = 40
sum_alphabet_indices("a dog 3!") # --> 0 + 3 + 14 + 6 = 23
```
