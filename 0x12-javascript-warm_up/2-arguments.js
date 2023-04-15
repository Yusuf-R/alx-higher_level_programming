#!/usr/bin/node
const sArgv = require('process');
if (sArgv.argv.length < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
