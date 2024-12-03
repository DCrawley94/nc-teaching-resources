# Tuesday Code Discussion - Functions

**Emphasise that we do not expect all challenges to be completed - in fact it is very rare that they'll be able to complete everything and that is intentional**

Pick a few challenges, ask who's seen it/solved it and ask how they did it and ask for guidance in solving it.

**Show how to use google/speedsheet to find useful methods**

## Challenges

### **2**: is_absolute_path

- `startswith` e.g. string_1.startswith('abc')
- Could mention regex but don't solve with this.

### **3**: how_many_arguments

- Useful for showing variadic functions
- `*args`
- https://realpython.com/python-kwargs-and-args/

### **3**: update_coin_machine

- can show `dict.get` or `dict[x]`

### **3**: is_falsy

can show `not` - e.g. `return not x`

https://docs.python.org/3/reference/expressions.html#not -> "The operator not yields True if its argument is false, False otherwise."

- In programming, truthy and falsy describe how values behave in logical conditions, like an if statement.
- A truthy value evaluates to True in a condition, while a falsy value evaluates to False.
  - Common falsy values in Python are 0, 0.0, "" (empty string), [] (empty list), {} (empty dictionary), set() (empty set), None, and False.
  - Everything else, like non-zero numbers, non-empty strings, and populated collections, is truthy.
- Think of it like this: Truthy means “has something,” and falsy means “empty or nothing.”

### **4**: check_if_key_exists

- `.get`

### **4**: get_first_n_items

- slice syntax

### **5**: find_total_of_multiples

- `range`
- `sum`
