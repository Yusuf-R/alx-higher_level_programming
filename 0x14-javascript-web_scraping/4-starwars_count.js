#!/usr/bin/node
// a script to print the title of a Star Wars movie
const request = require('request');
let count = 0;
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const resultsData = filmData.results;
    for (const i of resultsData) {
      const characterData = i.characters;
      for (const j of characterData) {
        if (j.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error in data:', response.statusCode);
    process.exit(1);
  }
});
