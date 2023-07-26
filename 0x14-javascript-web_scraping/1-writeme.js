#!/usr/bin/node
// a script to read the content of a file
const fs = require('fs');
const file = process.argv[2];
const string_to_write = process.argv[3];
fs.writeFile(file, string_to_write, 'utf-8', (err) => {
  if (err) {
    return console.log(err);
  }
});
