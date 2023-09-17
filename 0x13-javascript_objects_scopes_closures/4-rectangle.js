#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		for (let b = 0; b < this.height; b++) {
			let y = '';
			for (let c = 0; c < this.width; c++) {
				y += 'X';
			}
			console.log(y);
		}
	}

	rotate () {
		const temp = this.width;
		this.width = this.height;
		this.height = temp;
	}

	double () {
		this.width *= 2;
		this.height *= 2;
	}
}

module.exports = Rectangle;
