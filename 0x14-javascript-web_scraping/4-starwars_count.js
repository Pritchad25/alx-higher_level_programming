#!/usr/bin/node

//Imports the request module
const request = require('request');

//Using the request module to perform an HTTP GET request to the URL
request(process.argv[2], function (error, response, body) {
	//If there was no error during HTTP Request
	if (!error) {
		// parsing the JSON ata and extracting the results array
		const results = JSON.parse(body).results;
		//The reduce method is used to iterate through the movies
		//in the array
		console.log(results.reduce((count, movie) => {
			//if character with ID 18 is present, increment
			//count by 1, otherwise keep count as is.
			return movie.characters.find((character) => character.endsWith('/18/'))
			? count + 1
			: count;
		// reduce method strats with an initial value of 0
		}, 0));
	}
});
