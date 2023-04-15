#!/usr/bin/node
const sArgv = require('process');
if (sArgv.argv.length < 3) {
  console.log('No argument');
} else if (sArgv.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
