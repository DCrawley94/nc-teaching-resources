function handle400s(err, req, res, next) {
	console.log(err, ' <<< in middleware');
	if (err.code === '22P02' || err.code === '23502') {
		res.status(400).send({ msg: 'Bad Request' });
	} else if (err.code === '23503') {
		res.status(404).send({ msg: 'Not Found' });
	} else if (err.status === 404) {
		res.status(err.status).send({ msg: err.msg });
	} else {
		next(err);
	}
}

module.exports = { handle400s };
