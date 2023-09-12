#!/usr/bin/node
const SquareX = require('./5-square');

class Square extends SquareX {
	charPrint (c) {
		if (c === undefined) {
			c = 'X';
		}
		for (let d = 0; d < this.height; d++) {
			let z = '';
			for (let e = 0; e < this.width; e++) {
				z += c;
			}
			console.log(z);
		}
	}
}

module.exports = Square;
