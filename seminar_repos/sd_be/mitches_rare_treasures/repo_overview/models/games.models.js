const db = require('../db/connection');

function fetchGames() {
	return db.query('SELECT * FROM games;').then(({ rows }) => {
		return rows;
	});
}

function fetchGameById(id) {
	return db
		.query('SELECT * FROM games WHERE game_id = $1', [id])
		.then(({ rows }) => {
			if (rows.length === 0) {
				return Promise.reject({ status: 404, msg: 'Game Not Found' });
			}
			return rows[0];
		});
}

function insertGame(newGame) {
	const { game_title, release_year, console_name, image_url } = newGame;
	const queryStr = `
	INSERT INTO games
	(game_title, release_year, console_name, image_url)
	VALUES 
	($1, $2, $3, $4)
	RETURNING *`;

	return db
		.query(queryStr, [game_title, release_year, console_name, image_url])
		.then(({ rows }) => {
			return rows[0];
		});
}

function insertReview(newGame) {
	const { username, game_id, comment, rating } = newGame;
	const queryStr = `
	INSERT INTO reviews
	(username, game_id, comment, rating )
	VALUES 
	($1, $2, $3, $4)
	RETURNING *`;

	return db
		.query(queryStr, [username, game_id, comment, rating])
		.then(({ rows }) => {
			return rows[0];
		});
}

module.exports = { fetchGames, fetchGameById, insertGame, insertReview };
