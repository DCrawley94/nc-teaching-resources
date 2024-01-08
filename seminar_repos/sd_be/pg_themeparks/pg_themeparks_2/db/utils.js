function formatReviewsData(rawReviewData, insertedGameData) {
	const formattedReviewsData = rawReviewData.map((review) => {
		const gameWithID = insertedGameData.find((game) => {
			return game.game_title === review.game_title;
		});

		const reviewCopy = { ...review };
		reviewCopy.game_id = gameWithID.game_id;
		delete reviewCopy.game_title;
		return reviewCopy;
	});
	return formattedReviewsData;
}

module.exports = formatReviewsData;
