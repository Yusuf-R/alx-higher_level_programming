#!/usr/bin/node
const sArgv = require('process');
let count = 0;

for (const i of sArgv.argv) {
  count++;
}

if (count < 3) {
  console.log('No argument');
} else {
  const arg2 = sArgv.argv[2];
  console.log(arg2);
}
