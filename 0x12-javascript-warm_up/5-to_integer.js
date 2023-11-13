#!/usr/bin/node

// Getting the first argument from the command line
const arg = process.argv[2];

//convert the argument to integer
const intValue = parseInt(arg);

//let check if the result is not NaN
if (!isNaN(intValue)){
	console.log(`My number: ${intValue}`);
}else{
	console.log('Not a number');
}
