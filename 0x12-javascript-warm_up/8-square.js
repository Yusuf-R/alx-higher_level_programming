#!/usr/bin/node
const sysArgv = require('process');
const firstArg = sysArgv.argv[2];
const regMap = /^(\+|-)?\d+(\.\d+)?$/;
const isStrictInt = regMap.test(firstArg);
let msg = '';
if (isStrictInt) {
  const valNum = parseInt(firstArg);
  for (let i = 0; i < valNum; i++) {
    for (let j = 0; j < valNum; j++) {
      msg += 'X';
    }
    msg += '\n';
  }
  console.log(msg);
} else {
  console.log('Missing size');
}
