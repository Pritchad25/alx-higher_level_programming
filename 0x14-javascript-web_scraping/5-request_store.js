#!/usr/bin/node

//Impoting the fs module that is built-in in Node.js
const fs = require('fs');

//Importing the request module
const request = require('request');

//Using the request module to perform an HTTP GET request to the URL
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
