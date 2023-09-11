#!/usr/bin/node

// executeTimes.js
function executeTimes(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports.executeTimes = executeTimes;
