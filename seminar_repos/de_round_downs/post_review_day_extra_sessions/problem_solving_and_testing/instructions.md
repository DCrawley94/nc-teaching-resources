Advanced: Human Resources - remove_agents
It turns out Northcoders is riddled with corporate spies! It's become obvious to the resident conspiracy theorist that the moles signify their presence to each other on the company's social media platform's interests and about_me section.

If the about_me section or a single interest includes the letters m, o, l, e in that order, they are almost certainly a spy.

Your function should take a list of dictionaries representing users' social media profiles, and remove any suspected spies.

Do what you can.

```py
Examples of users to remove:

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
