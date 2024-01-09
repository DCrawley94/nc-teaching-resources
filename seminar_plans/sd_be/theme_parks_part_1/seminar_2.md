# Node PG: Data Formatting with TDD

Use data found [here](https://github.com/northcoders/team-curriculum/tree/main/curriculum/js-back-end/seeding-with-pg/staff/resources/example/db/data/test-data)

## Learning Objectives

- Be to identify when data needs to be manipulated before inserted into a database
- Know how to isolate a unit of logic in the seed function and test it

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
- **If not mentioned query students if there's any extra tests we might need as we're dealing with non-primitive data > if this has been mentioned ask why.**

## Actual Code

Show students repo with partial seed function, data, etc.

**Highlight the package.json script**

Show the created utils file and test suite ready to go.

With students help build up function with TDD.

## Possible tests and appropriate test data:

- empty array
- single review

```js
test('single review', () => {
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

	expect(formatReviewsData(reviewTestData, gameTestData)).toEqual(expectedData);
});
```

- multi review - single game

```js
test('multiple reviews - single game id', () => {
	const reviewTestData = [
		{
			username: 'fola',
			game_title: 'Mario Kart 64',
			comment: 'gingerbread',
			rating: 5
		},
		{
			username: 'rogersop',
			game_title: 'Mario Kart 64',
			comment: 'Skate',
			rating: 4
		},
		{
			username: 'izzi',
			game_title: 'Mario Kart 64',
			comment: 'Zombies',
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
		},
		{
			username: 'rogersop',
			game_id: 1,
			comment: 'Skate',
			rating: 4
		},
		{
			username: 'izzi',
			game_id: 1,
			comment: 'Zombies',
			rating: 5
		}
	];

	expect(formatReviewsData(reviewTestData, gameTestData)).toEqual(expectedData);
});
```

- multi review - multi game

```js
test('multiple reviews - multiple game ids', () => {
	const reviewTestData = [
		{
			username: 'fola',
			game_title: 'Mario Kart 64',
			comment: 'gingerbread',
			rating: 5
		},
		{
			username: 'rogersop',
			game_title: 'Donkey Kong',
			comment: 'Skate',
			rating: 4
		},
		{
			username: 'izzi',
			game_title: 'Mario Bros',
			comment: 'Zombies',
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
		},
		{
			game_id: 2,
			game_title: 'Donkey Kong',
			release_year: 1983,
			image_url:
				'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nes/nes_donkeykong_thumb.jpg',
			console_name: 'NES'
		},
		{
			game_id: 3,
			game_title: 'Mario Bros',
			release_year: 1985,
			image_url:
				'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nes/nes_mariobros_thumb.jpg',
			console_name: 'NES'
		}
	];
	const expectedData = [
		{
			username: 'fola',
			game_id: 1,
			comment: 'gingerbread',
			rating: 5
		},
		{
			username: 'rogersop',
			game_id: 2,
			comment: 'Skate',
			rating: 4
		},
		{
			username: 'izzi',
			game_id: 3,
			comment: 'Zombies',
			rating: 5
		}
	];

	expect(formatReviewsData(reviewTestData, gameTestData)).toEqual(expectedData);
});
```

- mutation

```js
test('input should not be mutated', () => {
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

	formatReviewsData(reviewTestData, gameTestData);

	expect(reviewTestData).toEqual([
		{
			username: 'fola',
			game_title: 'Mario Kart 64',
			comment: 'gingerbread',
			rating: 5
		}
	]);

	expect(gameTestData).toEqual([
		{
			game_id: 1,
			game_title: 'Mario Kart 64',
			release_year: 1996,
			image_url:
				'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nintendo_64/n64_mariokart64gold_thumb.jpg',
			console_name: 'N64'
		}
	]);
});
```

- reference?

Possible Solution:

```js
function formatReviewsData(rawReviewData, insertedGameData) {
	const formattedReviewsData = rawReviewData.map((review) => {
		const gameWithID = insertedGameData.find((game) => {
			return game.game_title === review.game_title;
		});

		const reviewCopy = { ...review };
		reviewCopy.game_id = gameWithID.game_id;
		delete reviewCopy.game_title;
		return reviewCopy;
	});
	return formattedReviewsData;
}

module.exports = formatReviewsData;
```

**If using find talk about a refactor to lookup object as it's more efficient**

```js
// seed.js
.then((gameInsertionResult) => {
			console.log('games inserted', gameInsertionResult);
			const insertedGames = gameInsertionResult.rows;
			const formattedReviewData = formatReviewsData(reviewData, insertedGames);

			return insertReviews(formattedReviewData);
		})
		.then(({ rows }) => {
			console.log({ rows });
		});
```
