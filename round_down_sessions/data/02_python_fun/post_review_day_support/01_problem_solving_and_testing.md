# Post Review Day - Problem Solving Refresher

**This one was quite beefy but lead to some good discussions about simplifying logic and when to break out into util functions**

Problem: https://l2c.northcoders.com/courses/de2-fun/review#sectionId=Advanced_Tasks,step=intro

Advanced: Human Resources - remove_agents
It turns out Northcoders is riddled with corporate spies! It's become obvious to the resident conspiracy theorist that the moles signify their presence to each other on the company's social media platform's interests and about_me section.

If the about_me section or a single interest includes the letters m, o, l, e in that order, they are almost certainly a spy.

Your function should take a list of dictionaries representing users' social media profiles, and remove any suspected spies.

Do what you can.

Examples of users to remove:

```py
 sam = {
   'name': 'Sam',
   'age': 30,
   'about_me': 'I have no personality! :D',
   'interests': ['code', 'guacamole']
  }

  # removed because of the interest guacamole!

  mitch = {
    'name': 'Mitch',
    'age': 29,
    'about_me': 'I am not a mole - I am a human being!',
    'interests': ['Tudor hymns', 'dancing']
  }

  # removed because of the word mole in about_me!

  jonny = {
    'name': 'Jonny',
    'age': 32,
    'about_me': "I'm a father of two girls - it's great!",
    'interests': ['parenting']
  }

  # removed because about_me contains the letters m, o, l, e. In that order:
  # i'M a father Of two girLs - it's grEat"

  vel = {
    'name': 'Vel',
    'age': 28,
    'about_me': 'I love games!',
    'interests': ['Magic', 'Monopoly Express']
  }

  # removed because the interest Monopoly Express contains the letters in the correct order.
```

---

Possible test breakdown:

- no issues with employee
- whole word mole found in about me
- whole word mole found in interests list
- letters spelling mole found in about me - all lowercase
- letters spelling mole found in interests - all lowercase
- moles with capital letters:
  - in about me (whole word)
  - in interests (whole word)
  - in about me (separate letters)
  - in interests (separate letters)
