#!/usr/bin/node
// a script to read the content of a file
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
