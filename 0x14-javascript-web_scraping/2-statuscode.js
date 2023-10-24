#!/usr/bin/node

const request = require('request');
//The line below imports the 'request' module.

request.get(process.argv[2])
//Using the request module to perform an HTTP GET request to the URL.

	.on('response', function (response) {
		//Setting up an event listener for the response
		console.log(`code: ${response.statusCode}`);
		//write theHTTP status code of response to the console
});
