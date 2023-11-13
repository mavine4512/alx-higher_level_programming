#!/usr/bin/node
const myObject = {
	type: 'object',
	value: 12
};

console.log(myObject);

const updateObject = {...myObject, value:89 };

console.log(updateObject);
