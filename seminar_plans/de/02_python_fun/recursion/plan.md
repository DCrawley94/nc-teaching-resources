# Recursion

**Figjam**: https://www.figma.com/file/kQdwksC4zZUpRRNGVoo73M/Recursion?type=whiteboard&node-id=0-1&t=pKXaFcgAODJnWHAw-0

## Learning Objectives

- Understand when Recursion is necessary
- Know the 3 components of a recursive function

## Intro - A Use Case for Recursion

**Nested Data Structures**

A common use case for recursion is for accessing or manipulating nested data structures.

Take a look at the following example:

```py
{
  "a": {
    "desired_data": "this is some very important data"
  },
  "b": {
    "c": {
      "desired_data": "this is some very important data"
    }
  },
  "d": {
    "e": {
      "f": {
        "g": {
          "desired_data": "this is some very important data"
        }
      }
    }
  }
}
```

- Let's say I want to access certain data from a nested object
- **But** I don't know how deep the nesting is
- **Recursion can be useful to help me traverse the nested structure and find the information I want**
- This is helpful as while I could use an iterative solution that would likely get very messy with lots of nested loops.

---

**🏁 CHECKPOINT 🏁**

---

## Introduce the Problem:

**count_ice_creams**

create a function that accepts an list as an argument, this list will either contain strings or lists which can also contain strings. The function should count the number of times a string of "ice cream" appears inside these lists.

```py
count_ice_creams(['banana', 'ice cream']) # 1

count_ice_creams(['banana', 'ice cream', ['tofu', ['ice cream']], 'ice cream']) # 3
```

**❗ After talking through ask students why we might need recursion here ❗**

Explain that any recursive solution can be written instead in an iterative way - it's just that this can quickly get out of hand.

---

**🏁 CHECKPOINT 🏁**

---

## Solving the Problem

Before moving to VSCode ask students what they think the base case/ recursive case/ recursive step might be.

**Base case**: when there are no nested lists - the counting occurs within the for loop
**Recursive case**: when there is a nested list - perform a recursive step to count values in that list and add to the total
**Recursive step**: by passing a nested list each time, we eventually get closer to the lowest level of nesting (our base case)
ay.
**Recursive call**: call self

### Test 1: Single element list returns 1 or 0

```py
def test_non_nested_list_no_ice_cream():
    assert count_ice_creams(["not ice cream"]) == 0


def test_non_nested_list_single_ice_cream():
    assert count_ice_creams(["ice cream"]) == 1
```

No recursion required:

**ASK STUDENT TO DIRECT ME IN A SOLUTION**

```py
def count_ice_creams(food_list):
    count = 0

    for food in food_list:
        if food == 'ice cream':
            count += 1

    return count
```

### Test 2: Multi element list returns count of ice creams

```py
def test_non_nested_list_multiple_ice_creams():
    some_ice_creams = ["ice cream", "banana", "ice cream", "apple"]
    assert count_ice_creams(some_ice_creams) == 2
```

**Same solution - force a fail**

```py
def count_ice_creams(food_list):
    count = 0

    for food in food_list:
        if food == 'ice cream':
            count += 1

    return count
```

### Test 3: Nested single Ice Creams

```py
def test_nested_list_single_item():
    nested_ice_cream = [["ice cream"]]
    assert count_ice_creams(nested_ice_cream) == 1
```

### Test 4: Extra Nested single Ice Creams

```py
def test_extra_nested_list_single_item():
    nested_ice_cream = [[["ice cream"]]]
    assert count_ice_creams(nested_ice_cream) == 1
```

**Ask if students want to see a nested for loop solution**

Possible for loop solution:

```py
def count_ice_creams(food_list):
    count = 0

    for el in food_list:
        if el == 'ice cream':
            count += 1
        elif isinstance(el, list):
            nested_food_list = el
            for nested_el in nested_food_list:
                if nested_el == 'ice cream':
                    count += 1
                elif isinstance(nested_el, list):
                    extra_nested_food_list = nested_el
                    for extra_nested_el in extra_nested_food_list:
                        if extra_nested_el == 'ice cream':
                            count += 1

    return count
```

**Let's refactor this:**

```py
def count_ice_creams(food_list):
    count = 0

    for item in food_list:
        if isinstance(item, list):
            return count_ice_creams(item)
        elif item == 'ice cream':
            count += 1

    return count
```

**Can work step through this test with the debugger if students are confused**

### Test 5: Varied nested Ice Creams

```py
def test_multiple_nested_items_varied_nesting():
    varied_nesting_search = [
        ["ice cream"],
        "sadness",
        [["ice cream"], "sadness"],
        [[["ice cream", "sadness"], "ice cream"]],
    ]

    assert count_ice_creams(varied_nesting_search) == 4
```

Before solving this ask why our previous solution didn't work and explore it with the debugger - highlight the issue of the early return.

Solution:

```py
def count_ice_creams(food_list):
    count = 0

    for item in food_list:
        if isinstance(item, list):
            count += count_ice_creams(item)
        elif item == 'ice cream':
            count += 1

    return count
```

## Debugger

To round of the session run the final test with the debugger. Set the breakpoint to be on the first line of the function body.

Step through and identify each time what is happening and what variables we have stored etc.

```py
[
	['ice cream'],
	'sadness',
	[['ice cream'], 'sadness'],
	[[['ice cream', 'sadness'], 'ice cream']]
];
```

- INITIAL INVO
- list and count vars declared
- for loop - gloss over item var
- first el: count is reassigned to be current val + result of calling count_ice_creams (**SHOW BY LEAVING COUNT WITH NO VALUE FOR NOW**)
  - SECOND CALL
  - list and count vars declared
  - for loop
  - single element ice cream > count var incremented
  - count returned
- count variable is reassigned to be `1`
- Next el skipped over because no list an no ice cream
- Next el is list: count is reassigned to be current val + result of calling count_ice_creams
  - THIRD CALL
  - list and count vars declared
  - for loop
  - Next el is list: count is reassigned to be current val + result of calling count_ice_creams
    - FOURTH CALL
    - list and count vars declared
    - for loop
    - single element ice cream > count var incremented
    - count returned
  - count variable is reassigned to be `1`
  - Next el skipped over because no list an no ice cream
  - count returned
- count variable is reassigned to be `2`
- Next el is list: count is reassigned to be current val + result of calling count_ice_creams
  - FIFTH CALL
  - list and count vars declared
  - for loop
  - Next el is list: count is reassigned to be current val + result of calling count_ice_creams
    - SIXTH CALL
    - list and count vars declared
    - for loop
    - Next el is list: count is reassigned to be current val + result of calling count_ice_creams
      - SEVENTH CALL
      - list and count vars declared
      - for loop
      - Next el is ice cream
      - count incremented
      - next el is not ice cream - skipped
      - return count
    - count is reassigned to be `1`
    - Next el is ice cream
    - count incremented to `2`
    - return count
  - count is reassigned to be `2`
  - count returned
- count variable is reassigned to be `4`
- count returned
- FINAL OUTPUT IS 4
