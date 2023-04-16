#!/usr/bin/node
const sysArgv = require('process');
let msg = '';
if (sysArgv.argv[2]) {
  const count = sysArgv.argv[2];
  for (let i = 0; i < count; i++) {
    for (let j = 0; j < count; j++) {
      msg = msg + 'X';
    }
    msg += '\n';
  }
  console.log(msg);
} else if (!sysArgv.argv[2]) {
  console.log('Missing size');
}
