#!/usr/bin/node
const lenVec = process.argv.length;
const arrInput = [];
let i = 0;
if (lenVec < 4) {
  console.log(0);
} else {
  for (i = 2; i < lenVec; i++) {
    if (isNaN(process.argv[i])) {
      console.log(0);
      break;
    } else {
      arrInput.push(parseInt(process.argv[i]));
    }
  }
  const arrLen = arrInput.length;
  let m2 = 0;
  if (arrLen === 2) {
    m2 = arrInput[0];
    if (arrInput[0] > arrInput[1]) {
      m2 = arrInput[1];
    }
  } else {
    i = 0;
    let max = 0;
    let idx = 0;
    while (i < arrLen) {
      if (max < arrInput[i]) {
        max = arrInput[i];
        idx = i;
      }
      i++;
    }
    i = -1;
    while (i < arrLen) {
      i++;
      if (i === idx) {
        continue;
      } else {
        if (m2 < arrInput[i]) {
          m2 = arrInput[i];
        }
      }
    }
  }
  console.log(m2);
}
