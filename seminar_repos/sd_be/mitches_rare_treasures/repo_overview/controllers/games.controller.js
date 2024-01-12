const {
	fetchGames,
	fetchGameById,
	insertGame,
	insertReview
} = require('../models/games.models');

function getGames(req, res) {
	fetchGames()
		.then((games) => {
			res.status(200).send({ games });
		})
		.catch((err) => {
			next(err);
		});
}

function getGameById(req, res, next) {
	const { gameId } = req.params;
	fetchGameById(gameId)
		.then((game) => {
			res.status(200).send({ game });
		})
		.catch((err) => {
			next(err);
		});
}

function postGame(req, res, next) {
	const newGame = req.body;
	insertGame(newGame)
		.then((game) => {
			res.status(201).send({ game });
		})
		.catch((err) => {
			next(err);
		});
}

function postReview(req, res, next) {
	const newReview = req.body;
	insertReview(newReview).then((review) => {
		res.status(201).send({ review });
	});
}

module.exports = { getGames, getGameById, postGame, postReview };
