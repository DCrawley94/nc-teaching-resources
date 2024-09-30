const express = require('express');
const {
	getGames,
	getGameById,
	postGame
} = require('./controllers/games.controller');

const app = express();

app.get('/api/games', getGames);
app.post('/api/games', postGame);
app.get('/api/games/:gameId', getGameById);

app.use((err, req, res, next) => {
	if (err.code === '22P02') {
		res.status(400).send({ err: 'Bad request' });
	} else if (err.status === 404) {
		res.status(err.status).send({ msg: err.msg });
	}
	next(err);
});

app.use((err, req, res, next) => {
	console.log(err);
	res.status(500).send({ msg: 'Internal Server Error' });
});

module.exports = app;
