#!/usr/bin/node
// a script to display the staus code of GET request
const request = require('request');
const url = process.argv[2];
request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
