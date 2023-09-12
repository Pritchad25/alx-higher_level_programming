#!/usr/bin/node
exports.esrever = function (list) {
	let length = list.length - 1;
	let g = 0;
	while ((length - g) > 0) {
		const aux = list[length];
		list[length] = list[g];
		list[g] = aux;
		g++;
		length--;
	}
	return list;
};
