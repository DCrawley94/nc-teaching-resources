const formatReviewsData = require('../db/utils');

describe('formatReviewsData', () => {
	test('no reviews - return empty array', () => {
		expect(formatReviewsData([], [])).toEqual([]);
	});
	test('single review', () => {
		const reviewTestData = [
			{
				username: 'fola',
				game_title: 'Mario Kart 64',
				comment: 'gingerbread',
				rating: 5
			}
		];
		const gameTestData = [
			{
				game_id: 1,
				game_title: 'Mario Kart 64',
				release_year: 1996,
				image_url:
					'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nintendo_64/n64_mariokart64gold_thumb.jpg',
				console_name: 'N64'
			}
		];

		const expected = [
			{
				username: 'fola',
				game_id: 1,
				comment: 'gingerbread',
				rating: 5
			}
		];

		expect(formatReviewsData(reviewTestData, gameTestData)).toEqual(expected);
	});
	test('multiple reviews - same game id', () => {
		const reviewTestData = [
			{
				username: 'fola',
				game_title: 'Mario Kart 64',
				comment: 'gingerbread',
				rating: 5
			},
			{
				username: 'rogersop',
				game_title: 'Mario Kart 64',
				comment: 'Skate',
				rating: 4
			},
			{
				username: 'izzi',
				game_title: 'Mario Kart 64',
				comment: 'Zombies',
				rating: 5
			}
		];
		const gameTestData = [
			{
				game_id: 1,
				game_title: 'Mario Kart 64',
				release_year: 1996,
				image_url:
					'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nintendo_64/n64_mariokart64gold_thumb.jpg',
				console_name: 'N64'
			}
		];
		const expectedData = [
			{
				username: 'fola',
				game_id: 1,
				comment: 'gingerbread',
				rating: 5
			},
			{
				username: 'rogersop',
				game_id: 1,
				comment: 'Skate',
				rating: 4
			},
			{
				username: 'izzi',
				game_id: 1,
				comment: 'Zombies',
				rating: 5
			}
		];
		expect(formatReviewsData(reviewTestData, gameTestData)).toEqual(
			expectedData
		);
	});
	test('multiple reviews - multiple game ids', () => {
		const reviewTestData = [
			{
				username: 'fola',
				game_title: 'Mario Kart 64',
				comment: 'gingerbread',
				rating: 5
			},
			{
				username: 'rogersop',
				game_title: 'Donkey Kong',
				comment: 'Skate',
				rating: 4
			},
			{
				username: 'izzi',
				game_title: 'Mario Bros',
				comment: 'Zombies',
				rating: 5
			}
		];
		const gameTestData = [
			{
				game_id: 1,
				game_title: 'Mario Kart 64',
				release_year: 1996,
				image_url:
					'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nintendo_64/n64_mariokart64gold_thumb.jpg',
				console_name: 'N64'
			},
			{
				game_id: 2,
				game_title: 'Donkey Kong',
				release_year: 1983,
				image_url:
					'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nes/nes_donkeykong_thumb.jpg',
				console_name: 'NES'
			},
			{
				game_id: 3,
				game_title: 'Mario Bros',
				release_year: 1985,
				image_url:
					'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nes/nes_mariobros_thumb.jpg',
				console_name: 'NES'
			}
		];
		const expectedData = [
			{
				username: 'fola',
				game_id: 1,
				comment: 'gingerbread',
				rating: 5
			},
			{
				username: 'rogersop',
				game_id: 2,
				comment: 'Skate',
				rating: 4
			},
			{
				username: 'izzi',
				game_id: 3,
				comment: 'Zombies',
				rating: 5
			}
		];

		expect(formatReviewsData(reviewTestData, gameTestData)).toEqual(
			expectedData
		);
	});
	test('input should not be mutated', () => {
		const reviewTestData = [
			{
				username: 'fola',
				game_title: 'Mario Kart 64',
				comment: 'gingerbread',
				rating: 5
			}
		];
		const gameTestData = [
			{
				game_id: 1,
				game_title: 'Mario Kart 64',
				release_year: 1996,
				image_url:
					'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nintendo_64/n64_mariokart64gold_thumb.jpg',
				console_name: 'N64'
			}
		];

		formatReviewsData(reviewTestData, gameTestData);

		expect(reviewTestData).toEqual([
			{
				username: 'fola',
				game_title: 'Mario Kart 64',
				comment: 'gingerbread',
				rating: 5
			}
		]);
		expect(gameTestData).toEqual([
			{
				game_id: 1,
				game_title: 'Mario Kart 64',
				release_year: 1996,
				image_url:
					'https://coverproject.sfo2.cdn.digitaloceanspaces.com/nintendo_64/n64_mariokart64gold_thumb.jpg',
				console_name: 'N64'
			}
		]);
	});
});
