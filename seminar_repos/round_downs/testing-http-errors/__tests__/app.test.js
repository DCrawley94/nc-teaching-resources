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
		test('should body should contain an array of game objects', () => {
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
		// ID - valid but non-existant e.g. /api/games/1000
		test('Status Code 404 - game not found', () => {
			return request(app)
				.get('/api/games/1000')
				.expect(404)
				.then(({ body }) => {
					expect(body.err).toBe('Game not found');
				});
		});
		// Non-valid ID e.g. /api/games/banana
		test('status code 400 - bad request - non valid id', () => {
			return request(app)
				.get('/api/games/banana')
				.expect(400)
				.then(({ body }) => {
					expect(body.err).toBe('Bad request');
				});
		});
	});
});
