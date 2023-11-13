#!/usr/bin/node
const [a, b] = process.argv.slice(2);
const add = (x, y) => parseInt(x) + parseInt(y);

console.log(add(a, b));
