#!/usr/bin/node
const dict = require('./101-data').dict;

const totalList = Object.entries(dict);
const value = Object.values(dict);
const valsUnique = [...new Set(value)];
const newDict = {};
for (const a in valsUnique) {
	const list = [];
	for (const b in totalList) {
		if (totalList[b][1] === valsUnique[a]) {
			list.unshift(totalList[b][0]);
		}
	}
	newDict[valsUnique[a]] = list;
}
console.log(newDict);
