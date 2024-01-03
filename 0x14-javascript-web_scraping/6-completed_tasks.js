#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, {json: true}, (error, response, body) => {
	if (error) {
		console.log(error);
		return;
	}

	const tasksCompleted = {};
	body.forEach((todo) => {
		if (todo.completed) {
			if (!taskCompleted[todo.userId]){
				taskCompleted[todo.userId] = 1;
			} else {
				taskCompleted[todo.userId] += 1;
			}
		}
	});
	console.log(tasksCompleted);
});
