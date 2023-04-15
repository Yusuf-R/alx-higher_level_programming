#!/usr/bin/node
const sysArgv = require('process');
if (sysArgv.argv[2]) {
  console.log(sysArgv.argv[2]);
} else {
  console.log('No argument');
}
