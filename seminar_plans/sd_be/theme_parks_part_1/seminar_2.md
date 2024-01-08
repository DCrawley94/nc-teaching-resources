# Node PG: Data Formatting with TDD

Use data found [here](https://github.com/northcoders/team-curriculum/tree/main/curriculum/js-back-end/seeding-with-pg/staff/resources/example/db/data/test-data)

## Learning Objectives

- Know when

## Intro

Resources:

- seed function pre-written to insert games data
- DB Diagram showing DB structure - use a screenshot in Figjam
- Table showing what data we have ready for insertion

Ask students to think about what we have and what we need to do.

**Can they foresee a problem if we were to insert the reviews data as is?**

**Ask them to think on how we might tackle this problem**

**Ask students for help in pseudocoding out a bit of a solution at a high level**

Example:

```js
// Take existing games data and raw review data
// add game_id property to each review
// this game id comes from inserted game data
// delete existing game_title property
```

Explain that this is some reasonably complex logic and as such we should extract it out into it's own function. This will then enable us to use TDD to ensure that this logic as working as it should.

❗ _Highlight that this is an example of the relevance of testing in a larger context._

❗ _We can isolate a unit of code and test it in isolation._

❗ _This gives us increased confidence in our code and should enable us to iron out any possible bugs._

Whiteboard out the solution:

- ask students what the function should take accept as arguments
- put previous pseudocode in the function
- Ask students to think about what tests they might write for this, take suggestions and note them down
- If not mentioned query students if there's any extra tests we might need as we're dealing with non-primitive data > if this has been mentioned ask why.

## Actual Code

Show students repo with partial seed function, data, etc. Show the created utils file and test suite ready to go.

With students help build up function with TDD.

## Possible tests and appropriate test data:

- empty array
- single review

data:

```js
const reviewTestData = [
	{
		username: 'fola',
		game_title: 'Mario Kart 64',
		comment: 'gingerbread',
		rating: 5
	}
];
const gameTestData = [
	{
		game_id: 1,
		game_title: 'Mario Kart 64',
		release_year: 1996,
		image_url:
			'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nintendo_64/n64_mariokart64gold_thumb.jpg',
		console_name: 'N64'
	}
];
const expectedData = [
	{
		username: 'fola',
		game_id: 1,
		comment: 'gingerbread',
		rating: 5
	}
];
```

- multi review - single game
- multi review - multi game
- mutation
- reference?
