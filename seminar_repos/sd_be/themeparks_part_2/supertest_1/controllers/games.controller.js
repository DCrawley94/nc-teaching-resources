const { fetchGames, fetchGameById } = require('../models/games.models');

function getGames(req, res) {
	fetchGames().then((games) => {
		res.status(200).send({ games });
	});
}

function getGameById(req, res) {
	const { gameId } = req.params;
	fetchGameById(gameId).then((game) => {
		res.status(200).send({ game });
	});
}

module.exports = { getGames, getGameById };
