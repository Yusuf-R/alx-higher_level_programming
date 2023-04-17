#!/usr/bin/node
module.exports.callMeMoby = function (x, theFunction) {
  for (let iter = 0; iter < x; iter++) {
    theFunction();
  }
};
