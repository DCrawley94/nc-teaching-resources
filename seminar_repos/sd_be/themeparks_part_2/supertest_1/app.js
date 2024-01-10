const express = require('express');
const { getGames, getGameById } = require('./controllers/games.controller');

const app = express();

app.get('/api/games', getGames);
app.get('/api/games/:gameId', getGameById);

module.exports = app;
