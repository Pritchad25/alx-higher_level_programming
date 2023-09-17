#!/usr/bin/node
let numberOfArg = 0;

exports.logMe = function (item) {
	console.log(numberOfArg+ ': ' + item);
	numberOfArg++;
};
