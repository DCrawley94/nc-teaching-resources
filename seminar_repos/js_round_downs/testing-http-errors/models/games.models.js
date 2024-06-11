const db = require('../db/connection');

function fetchGames() {
	return db.query('SELECT * FROM games;').then(({ rows }) => {
		return rows;
	});
}

function insertGame(game) {
	return db
		.query(
			'INSERT INTO games (game_title, release_year, image_url, console_name) VALUES ($1, $2, $3, $4) RETURNING *;',
			[game.game_title, game.release_year, game.console_name, image_url]
		)
		.then(({ rows }) => {
			return rows[0];
		})
		.catch((err) => {
			console.log(err);
		});
}

function fetchGameById(id) {
	return db
		.query('SELECT * FROM games WHERE game_id = $1', [id])
		.then(({ rows }) => {
			if (rows.length === 0) {
				return Promise.reject({ err: 'Game not found' });
			}
			return rows[0];
		});
}

module.exports = { fetchGames, fetchGameById, insertGame };
