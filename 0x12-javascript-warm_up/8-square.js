#!/usr/bin/node
const sysArgv = require('process');
const firstArg = sysArgv.argv[2];
const regMap = /^(\+|-)?\d+(\.\d+)?$/;
const isStrictInt = regMap.test(firstArg);
let msg = '';
if (isStrictInt) {
  const valNum = parseInt(firstArg);
  if (valNum < 0) {
    console.log();
  } else if (valNum >= 0) {
    for (let i = 0; i < valNum; i++) {
      for (let j = 0; j < valNum; j++) {
        msg += 'X';
      }
      msg += '\n';
    }
    msg = msg.trim();
    console.log(msg);
  }
} else {
  console.log('Missing size');
}
