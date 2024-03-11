'''
 - function take a string as an argument 
 - function will return a number 
 - that number will be the summed value of the index positions of the strings characters, 
      as they appear in the alphabet (taking into account zero indexing). 
 - function will ignore characters that are not lower case letters

 Examples 
 sum_alphabet_indices("") --> 0
 sum_alphabet_indices("a") --> 0
 sum_alphabet_indices("hello") --> 7 + 4 + 11 + 11 + 14 = 47 
 sum_alphabet_indices("Hello") --> 4 + 11 + 11 + 14 = 40
 sum_alphabet_indices("a dog 3!") --> 0 + 3 + 14 + 6 = 23
'''

import string


def sum_alphabet_indices(sentence):
    lowercase_letters = string.ascii_lowercase

    return sum([lowercase_letters.find(char) for char in sentence if char in lowercase_letters])
