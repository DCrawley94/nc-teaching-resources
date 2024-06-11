const seed = require('./seed.js');
const db = require('./connection.js');
const data = require('./data/dev_data/index.js');

seed(data).then(() => {
	return db.end();
});
