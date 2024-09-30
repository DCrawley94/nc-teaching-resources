const db = require('./connection');
const format = require('pg-format');

const formatReviewsData = require('./utils');

function seed({ gameData, reviewData }) {
	return db
		.query('DROP TABLE IF EXISTS reviews;')
		.then(() => {
			return db.query('DROP TABLE IF EXISTS games;');
		})
		.then(() => {
			return createGames();
		})
		.then(() => {
			return createReviews();
		})
		.then(() => {
			return insertGames(gameData);
		})
		.then(({ rows: insertedGamesData }) => {
			const formattedReviews = formatReviewsData(reviewData, insertedGamesData);

			return insertReviews(formattedReviews);
		});
}

function createGames() {
	return db.query(
		`CREATE TABLE games (
			game_id SERIAL PRIMARY KEY,
			game_title VARCHAR NOT NULL,
			release_year INT,
			image_url VARCHAR, 
			console_name VARCHAR NOT NULL
			);`
	);
}

function createReviews() {
	return db.query(
		`CREATE TABLE reviews (
			review_id SERIAL PRIMARY KEY,
			game_id INT NOT NULL REFERENCES games(game_id),
			username VARCHAR NOT NULL,
			comment VARCHAR NOT NULL,
			rating INT
		);`
	);
}

function insertGames(gameData) {
	const gamesToInsert = gameData.map((game) => [
		game.game_title,
		game.release_year,
		game.image_url,
		game.console_name
	]);
	const queryStr = format(
		`INSERT INTO games
			(game_title, release_year, image_url, console_name)
			VALUES
			%L
		RETURNING *;`,
		gamesToInsert
	);
	return db.query(queryStr);
}

function insertReviews(reviewData) {
	const reviewsToInsert = reviewData.map((review) => [
		review.username,
		review.game_id,
		review.comment,
		review.rating
	]);
	const queryStr = format(
		`INSERT INTO reviews
			(username, game_id, comment, rating)
			VALUES
			%L
			RETURNING *;`,
		reviewsToInsert
	);
	return db.query(queryStr);
}

module.exports = seed;
