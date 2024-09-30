function formatReviewsData(rawReviewData, insertedGameData) {
	const formattedReviewData = rawReviewData.map((review) => {
		const gameMatch = insertedGameData.find((game) => {
			return game.game_title === review.game_title;
		});
		const id = gameMatch.game_id;

		const newReviewObject = { ...review };

		newReviewObject.game_id = id;
		delete newReviewObject.game_title;

		return newReviewObject;
	});

	return formattedReviewData;
}

module.exports = formatReviewsData;
