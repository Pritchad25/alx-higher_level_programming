#!/usr/bin/node

const fs = require('fs');
//The code below imports the 'fs' module that is built in in Nodejs

fs.readFile(process.argv[2], 'utf8', function (error, content) {
	if (error) {
		console.error('Error reading the file:', error);
	} else {
		//if successfully read, content contains the contents of the file
		console.log(content);
	}
});
