#!/usr/bin/node
// a script to print the title of a Star Wars movie
const request = require('request');
const usrId = process.argv[2];

const id = parseInt(usrId, 10);

if (isNaN(id)) {
  console.log('Error in id: id must be int');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const moveiData = JSON.parse(body);
    console.log(moveiData.title);
  } else {
    console.log('Error in data:', response.statusCode);
    process.exit(1);
  }
});
