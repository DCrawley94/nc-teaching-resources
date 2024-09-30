const express = require('express');
const {
	getGames,
	getGameById,
	postGame,
	postReview
} = require('./controllers/games.controller');
const { handle400s } = require('./errorHandlers');

const app = express();

app.use(express.json());

app.get('/api/games', getGames);
app.post('/api/games', postGame);

app.get('/api/games/:gameId', getGameById);

app.post('/api/reviews', postReview);

app.use(handle400s);

app.use((err, req, res, next) => {
	console.log(err);
	res.status(500).send({ msg: 'Internal Server Error' });
});

module.exports = app;
