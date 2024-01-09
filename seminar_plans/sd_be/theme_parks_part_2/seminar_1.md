# Integration testing and Supertest

# Seminar 1: Testing for GET requests.

## Learning Objectives

- Know how to use supertest to test a GET request

## Intro

Show the repo that will be used today.

Explain that some people may be familiar with it but essentially it has the following:

- a `seed` function that has been used to `seed` the database with data about
  - **video games**
  - **reviews** for those video games

Explain that we will be creating an API that will be accessing the `nc_games` database.

During the lecture we will be writing the following two endpoints:

- `/api/games`
- `/api/games/:gameId`

## Discuss tests for first endpoint - `/api/games`:

Ask students to think about what we could test and note down ideas in the test file:

- status code
- response body contents

```js
/// tests

test('should respond with status code 200', () => {
	return request(app).get('/api/games').expect(200);
});
```

**EXPLAIN WHY WE NEED TO CHECK ARRAY LENGTH IF DOING THIS**

```js
test('should respond with an array of game objects', () => {
	return request(app)
		.get('/api/games')
		.then(({ body }) => {
			const games = body.games;
			expect(Array.isArray(games)).toBe(true);
			expect(games.length).toBeGreaterThan(0);
			games.forEach((game) => {
				expect(typeof game.game_id).toBe('number');
				expect(typeof game.game_title).toBe('string');
				expect(typeof game.release_year).toBe('number');
				expect(typeof game.image_url).toBe('string');
				expect(typeof game.console_name).toBe('string');
			});
		});
});
```

---

## Solutions

---

```js
//app
app.get('/api/games', getGames);
```

```js
//controller
function getGames(req, res) {
	fetchGames().then((games) => {
		res.status(200).send({ games });
	});
}
```

```js
//model
function fetchGames() {
	return db.query('SELECT * FROM games;').then(({ rows }) => {
		return rows;
	});
}
```

Reminder on closing DB connection

```js
const db = require('../db/connection');

afterAll(() => {
	return db.end();
});
```

## Discuss tests for first endpoint - `/api/game/:game_id`:

Ask students to think about what we could test and note down ideas:

- status code
- response body contents

```js
test('should respond with status code 200', () => {
	return request(app).get('/api/games/1').expect(200);
});
test('should respond with a single game object with the correct id', () => {
	return request(app)
		.get('/api/games/1')
		.then(({ body }) => {
			const game = body.game;
			console.log({ game });

			expect(game.game_id).toBe(1);
			expect(game.game_title).toBe('Mario Kart 64');
			expect(game.release_year).toBe(1996);
			expect(game.console_name).toBe('N64');
			expect(game.image_url).toBe(
				'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nintendo_64/n64_mariokart64gold_thumb.jpg'
			);
		});
});
```

---

## Solutions

---

```js
// app
app.get('/api/games/:gameId', getGameById);
```

```js
// controller
function getGameById(req, res) {
	const { gameId } = req.params;
	fetchGameById(gameId).then((game) => {
		res.status(200).send({ game });
	});
}
```

```js
// model
function fetchGameById(id) {
	return db
		.query(`SELECT * FROM games WHERE game_id = $1;`, [id])
		.then(({ rows }) => {
			return rows[0];
		});
}
```

**Highlight the parametrised query - avoiding injection**

## If there's time

Jests Object containing:

https://jestjs.io/docs/expect#expectobjectcontainingobject
