#!/usr/bin/node

//Importing the request module
const request = require('request');

//Creating the URL for the specific StarWars file
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

//Using the request module to perform an HTTP GET request to the created URL
request(url, function (error, response, body) {
	//Write the title on success otherwise write error
	console.log(error || JSON.parse(body).title);
});
