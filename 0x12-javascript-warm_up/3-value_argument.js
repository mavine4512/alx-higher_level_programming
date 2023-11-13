#!/usr/bin/node

//checking id there are any arguments passed
if (process.argv[2] === undefined) {
	console.log('No argument');
} else {
	console.log(process.argv[2]);
}
