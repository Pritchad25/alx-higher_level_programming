#!/usr/bin/node

const fs = require('fs');
//importing the built-in Node.js 'fs' module.

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
	//Using fs.writeFile() to write data to a file that is third command line
	//argument (process.argv[2]). The data to be written is taken from
	//process.argv[3] the fourth command line argument

	if (error) {
		//error object will contain an error object in the case of an error occuring
		console.error(error);
	}
});
