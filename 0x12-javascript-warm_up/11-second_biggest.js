#!/usr/bin/node
const len_vec = process.argv.length
let arr_input = []
if (len_vec < 4) {
  console.log(0);
} else {
  for (let i = 2; i < len_vec; i++) {
    if (isNaN(process.argv[i])) {
      console.log(0);
      break;
    } else {
      arr_input.push(parseInt(process.argv[i]));
    }
  }
  const arrLen = arr_input.length;
  let m2 = 0;
  if (arrLen === 2) {
    m2 = arr_input[0];
    if (arr_input[0] > arr_input[1]) {
      m2 = arr_input[1];
    } else {
      m2 = m2;
    }
  } else {
    i = 0;
    let max = 0;
    let idx = 0;
    while (i < arrLen) {
      if (max < arr_input[i]) {
        max = arr_input[i];
        idx = i;
      } else {
        max = max;
        idx = idx;
      }
      i++; 
    }
    i = -1;
    while (i < arrLen) {
      i++;
      if (i === idx) {
        continue;
      } else {
        if (m2 < arr_input[i]) {
          m2 = arr_input[i];
        } else {
          m2 = m2;
          }
        }
      }
    }
  console.log(m2);
}
