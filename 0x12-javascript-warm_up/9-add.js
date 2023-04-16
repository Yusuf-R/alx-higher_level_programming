#!/usr/bin/node
function add (a, b) {
  return (a + b);
}

const sysArg = require('process');
const n1 = sysArg.argv[2];
const n2 = sysArg.argv[3];

const val1 = Number.parseInt(n1, 10);
const val2 = Number.parseInt(n2, 10);

const result = add(val1, val2);
console.log(result);
