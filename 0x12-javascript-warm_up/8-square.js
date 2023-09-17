#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
	console.log('Missing size');
} else {
	const a = Number(process.argv[2]);
	let f = 0;
	while (f < a) {
		console.log('X'.repeat(a));
		f++;
	}
}
