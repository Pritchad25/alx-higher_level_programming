#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];


const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
	if (!error && response.statusCode === 200) {
		const movieData = JSON.parse(body);
		const characterPromises = movieData.characters.map((characterUrl) => {
			return new Promise((resolve, reject) => {
				request(characterUrl, function (charError, charResponse, charBody) {
					if (!charError && charResponse.statusCode === 200) {
						const characterData = JSON.parse(charBody);
						resolve(characterData.name);
					} else {
						reject(new Error(`Error fetching character data: ${charError}`));
					}
				});
			});
		});

		Promise.all(characterPromises).then((characterNames) => {
			console.log(characterNames.join('\n'));
		})
		.catch((error) => {
			console.error(error.message);
		});
	} else {
		console.error('Error fetching movie data:', error);
	}
});
