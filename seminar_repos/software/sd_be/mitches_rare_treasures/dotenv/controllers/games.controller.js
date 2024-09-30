const { fetchGames, fetchGameById } = require('../models/games.models');

function getGames(req, res, next) {
	fetchGames()
		.then((games) => {
			res.status(200).send({ games });
		})
		.catch((err) => {
			next(err);
		});
}

function getGameById(req, res) {
	const { gameId } = req.params;
	fetchGameById(gameId)
		.then((game) => {
			res.status(200).send({ game });
		})
		.catch((err) => {
			next(err);
		});
}

module.exports = { getGames, getGameById };
