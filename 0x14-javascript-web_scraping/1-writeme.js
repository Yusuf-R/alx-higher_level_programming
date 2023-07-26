#!/usr/bin/node
// a script to read the content of a file
const fs = require('fs');
const file = process.argv[2];
const stringWrite = process.argv[3];
fs.writeFile(file, stringWrite, 'utf-8', (err) => {
  if (err) {
    return console.log(err);
  }
});
