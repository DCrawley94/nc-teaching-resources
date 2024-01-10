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
			return rows[0];
		});
}

module.exports = { fetchGames, fetchGameById };
