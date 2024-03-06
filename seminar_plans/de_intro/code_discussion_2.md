# Wednesday Code Discussion

# Part 1

**Start by addressing students working into the evenings**

**also remind them that they don't need to finish sprints, they can just move on to the next tasks**

## Mob problem solve - Section Two Challenges

```py
# QUESTION 2
# This function should take a string as an argument and return True if
#  every letter is upper case and False if at least one character is not

def is_all_upper_case():
    pass
```

**Pseudo:**

- take a string as an argument
- iterate over the list
- check is each character is uppercase

or

- use `isupper()`

---

```py
# QUESTION 3
# This function should take a string as its argument and return a
#  string consisting of all vowels found in the input (retaining the order)

def collect_the_vowels(str):
    pass
```

**Pseudo:**

- take a string as a parameter
- iterate over the string
- check if a character is a vowel
- gather vowels in a new list
- return list

---

```py
# QUESTION 4
# This function should take two arguments, an list and an index, and return
#  the element at that specified index

# The index provided may be equal to or greater than the length of the
#  given list. In this case, rather than counting past the end of the
#  list where there are no values, the indexing should be considered to
#  "loop back around" and continue from the start of the list

# For examples of this behaviour, look at the second group of tests below

def access_item(list, index):
    pass
```

**pseudo:**

- take a list and an index
- if index is less than length then return element
- if index is greater than length then reduce it until it is < length

---

```py
# This function takes an list of names.
# The function should return an list containing the names of the people who
#   aren't spies.
# Recent intelligence has revealed that all spies codenames include the
#   letters 's', 'p' or 'y'.
# You can't afford to take any chances, and all names that include those
#   letters should be removed.


def counter_spy(people):
    pass


def test_counter_spy_returns_an_empty_list_if_the_only_person_is_a_spy():
    assert counter_spy(['Simon']) == []


@pytest.mark.skip(reason="delete this line when you want to run this test")
def test_counter_spy_returns_a_list_with_all_spies_removed():
    assert counter_spy(['Simon', 'Cat', 'Kyle']) == ['Cat']
    assert counter_spy(['Simon', 'Cat', 'Kyle', 'Danika', 'Alex', 'Chon']) == [
        'Cat', 'Danika', 'Alex', 'Chon']
```
