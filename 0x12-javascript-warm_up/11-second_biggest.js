#!/usr/bin/node
const result = process.argv.length <= 3
	? 0
	: Math.max(...process.argv.slice(2).map(Number).sort((a, b) => a - b));
console.log(result);
