const {
	fetchGames,
	fetchGameById,
	insertGame
} = require('../models/games.models');

function getGames(req, res, next) {
	fetchGames()
		.then((games) => {
			res.status(200).send({ games });
		})
		.catch((err) => {
			next(err);
		});
}

function postGame(req, res, next) {
	const game = req.body;
	insertGame(game)
		.then((game) => {
			res.status(201).send({ game });
		})
		.catch((err) => {
			next(err);
		});
}

function getGameById(req, res, next) {
	const { gameId } = req.params;
	// check the validity
	fetchGameById(gameId)
		.then((game) => {
			res.status(200).send({ game });
		})
		.catch((err) => {
			next(err);
		});
}

module.exports = { getGames, getGameById, postGame };
