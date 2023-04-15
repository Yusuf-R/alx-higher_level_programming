#!/usr/bin/node
const sysArgv = require('process');
const firstArg = sysArgv.argv[2];
const regMap = /^(\+|-)?\d+(\.\d+)?$/;
const isStrictInt = regMap.test(firstArg);
if (isStrictInt) {
  const valNum = parseInt(firstArg);
  console.log('My number: ', valNum);
} else {
  console.log('Not a number');
}
