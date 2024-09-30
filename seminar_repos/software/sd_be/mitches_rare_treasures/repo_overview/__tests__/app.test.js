const app = require('../app');
const request = require('supertest');
const db = require('../db/connection');
const seed = require('../db/seed');
const testData = require('../db/data/test_data');

beforeEach(() => {
	return seed(testData);
});

afterAll(() => {
	return db.end();
});

describe('/api/games', () => {
	describe('GET', () => {
		test('Status code 200', () => {
			return request(app).get('/api/games').expect(200);
		});
		test('body should contain an array of game objects', () => {
			return request(app)
				.get('/api/games')
				.then(({ body }) => {
					const games = body.games;

					expect(Array.isArray(games)).toBe(true);
					expect(games.length).toBe(3);

					games.forEach((game) => {
						expect(typeof game.game_id).toBe('number');
						expect(typeof game.game_title).toBe('string');
						expect(typeof game.release_year).toBe('number');
						expect(typeof game.console_name).toBe('string');
						expect(typeof game.image_url).toBe('string');
					});
				});
		});
	});
	describe('POST', () => {
		test('Status code 201 - responds with new game', () => {
			const testGame = {
				game_title: 'Danikas Sick Game',
				release_year: 2024,
				console_name: 'Xbox 720',
				image_url: 'https://somewhere.com'
			};
			return request(app)
				.post('/api/games')
				.send(testGame)
				.expect(201)
				.then(({ body }) => {
					const { game } = body;
					expect(game.game_id).toBe(4);
					expect(game.game_title).toBe('Danikas Sick Game');
					expect(game.release_year).toBe(2024);
					expect(game.console_name).toBe('Xbox 720');
					expect(game.image_url).toBe('https://somewhere.com');
				});
		});
		test('Status Code 400 - malformed body', () => {
			const malformedGame = {
				game_title: 'Danikas Sick Game',
				release_year: 2024,
				image_url: 'https://somewhere.com'
			};
			return request(app)
				.post('/api/games')
				.send(malformedGame)
				.expect(400)
				.then(({ body }) => {
					expect(body.msg).toBe('Bad Request');
				});
		});
		test('Status Code 400 - incorrect column data types', () => {
			const malformedGame = {
				game_title: 'Danikas Sick Game',
				release_year: true,
				console_name: 'Xbox 720',
				image_url: 'https://somewhere.com'
			};
			return request(app)
				.post('/api/games')
				.send(malformedGame)
				.expect(400)
				.then(({ body }) => {
					expect(body.msg).toBe('Bad Request');
				});
		});
	});
});

describe('/api/games/:gameId', () => {
	describe('GET', () => {
		test('responds with status code 200', () => {
			return request(app).get('/api/games/1').expect(200);
		});
		test('body should contain single game object', () => {
			return request(app)
				.get('/api/games/1')
				.then(({ body }) => {
					const game = body.game;
					expect(game.game_id).toBe(1);
					expect(game.game_title).toBe('Mario Kart 64');
					expect(game.release_year).toBe(1996);
					expect(game.console_name).toBe('N64');
					expect(game.image_url).toBe(
						'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nintendo_64/n64_mariokart64gold_thumb.jpg'
					);
				});
		});
		test('Status Code 404 - ID valid but non existant', () => {
			return request(app)
				.get('/api/games/1000')
				.expect(404)
				.then(({ body }) => {
					expect(body.msg).toBe('Game Not Found');
				});
		});
		test.only('status code 400 - ID not valid', () => {
			return request(app)
				.get('/api/games/banana')
				.expect(400)
				.then(({ body }) => {
					expect(body.msg).toBe('Bad Request');
				});
		});
	});
});

describe('/api/reviews', () => {
	describe('POST', () => {
		test('Status Code 201 - responds with new review', () => {
			const testReview = {
				username: 'fola',
				game_id: 1,
				comment: 'blah blah blah',
				rating: 5
			};
			return request(app)
				.post('/api/reviews')
				.send(testReview)
				.expect(201)
				.then(({ body }) => {
					const { review } = body;
					expect(review.review_id).toBe(29);
					expect(review.username).toBe('fola');
					expect(review.game_id).toBe(1);
					expect(review.comment).toBe('blah blah blah');
					expect(review.rating).toBe(5);
				});
		});
	});
});
