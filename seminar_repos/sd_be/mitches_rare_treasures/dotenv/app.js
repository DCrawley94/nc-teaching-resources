const express = require('express');
const { getGames, getGameById } = require('./controllers/games.controller');

const app = express();

app.get('/api/games', getGames);
app.get('/api/games/:gameId', getGameById);

app.use((err, req, res, next) => {
	console.log(err);
	res.status(500).send({ msg: 'Internal Server Error' });
});

module.exports = app;
