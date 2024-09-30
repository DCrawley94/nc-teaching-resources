# Mutation Testing Refresher

Plan:

- Introduce problem with initial test written

- Pick on people to suggest incremental testing - if people suggest mutation testing kick it back for now

Test data:

```py
# Single person:
people = [{ "name": 'Simon', "age": 21, "location": 'Leeds' }]
expected = [{ "name": 'Simon', "age": 21, "location": 'Manchester' }]

# Multiple person:
people = [
		{ "name": 'Mick', "age": 21, "location": 'Liverpool-ish' },
		{ "name": 'August', "age": 21, "location": 'Ancoats' },
    { "name": 'Chon', "age": 21, "location": 'Nottingham' }
]

expected = [
		{ "name": 'Mick', "age": 21, "location": 'Manchester' },
		{ "name": 'August', "age": 21, "location": 'Manchester' },
		{ "name": 'Chon', "age": 21, "location": 'Manchester' }
]
```

```py
def test_2():
    people = [{ "name": 'Simon', "age": 21, "location": 'Leeds' }]
    expected = [{ "name": 'Simon', "age": 21, "location": 'Manchester' }]

    result = move_to_manchester(people)

    assert result == expected

def test_3():
    people = [
		{ "name": 'Mick', "age": 21, "location": 'Liverpool-ish' },
		{ "name": 'August', "age": 21, "location": 'Ancoats' },
        { "name": 'Chon', "age": 21, "location": 'Nottingham' }
    ]
    expected = [
		{ "name": 'Mick', "age": 21, "location": 'Manchester' },
		{ "name": 'August', "age": 21, "location": 'Manchester' },
		{ "name": 'Chon', "age": 21, "location": 'Manchester' }
    ]

    result = move_to_manchester(people)

    assert result == expected
```
