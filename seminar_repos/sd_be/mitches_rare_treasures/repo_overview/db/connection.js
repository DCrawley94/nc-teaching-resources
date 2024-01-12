const { Pool } = require('pg');

const ENV = process.env.NODE_ENV || 'development';
const pathToCorrectEnvFile = `${__dirname}/../.env.${ENV}`;

require('dotenv').config({ path: pathToCorrectEnvFile });

if (!process.env.PGDATABASE) {
	throw new Error('No PGDATABASE configured');
}

module.exports = new Pool();
