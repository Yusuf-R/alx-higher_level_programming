#!/usr/bin/node
// a script to print the title of a Star Wars movie
const request = require('request');
const url = process.argv[2];

const usrIdDataCompleted = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const todoData = JSON.parse(body);
    todoData.forEach((element) => {
      const userId = element.userId;
      const completed = element.completed;
      if (!usrIdDataCompleted[userId]) {
        usrIdDataCompleted[userId] = 0;
      }
      if (completed) {
        usrIdDataCompleted[userId]++;
      }
    });
    console.log(usrIdDataCompleted);
  } else {
    console.log('Error in data:', response.statusCode);
    process.exit(1);
  }
});
