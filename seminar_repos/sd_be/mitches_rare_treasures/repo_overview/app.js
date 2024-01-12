const express = require('express');
const {
	getGames,
	getGameById,
	postGame,
	postReview
} = require('./controllers/games.controller');

const app = express();

app.use(express.json());

app.get('/api/games', getGames);
app.post('/api/games', postGame);

app.get('/api/games/:gameId', getGameById);

app.post('/api/reviews', postReview);

app.use((err, req, res, next) => {
	// console.log(err);
	if (err.code === '22P02' || err.code === '23502') {
		res.status(400).send({ msg: 'Bad Request' });
	} else if (err.code === '23503') {
		res.status(404).send({ msg: 'Not Found' });
	} else if (err.status === 404) {
		res.status(err.status).send({ msg: err.msg });
	} else {
		next(err);
	}
});

app.use((err, req, res, next) => {
	console.log(err);
	res.status(500).send({ msg: 'Internal Server Error' });
});

module.exports = app;
