#!/usr/bin/node
// a script to print the title of a Star Wars movie
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const lorem = body;
    fs.writeFile(filename, lorem, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log('Error in data:', response.statusCode);
    process.exit(1);
  }
});
