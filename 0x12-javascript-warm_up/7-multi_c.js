#!/usr/bin/node
const sysArgv = require('process');
const msg = 'C is fun';
if (sysArgv.argv[2]) {
  const count = sysArgv.argv[2];
  for (let i = 0; i < count; i++) {
    console.log(msg);
  }
} else if (!sysArgv.argv[2]) {
  console.log('Missing number of occurrences');
}
