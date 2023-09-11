#!/usr/bin/node

const X = parseInt(process.argv[2]);

if (!isNaN(X)) {
  for (let i = 0; i < X; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
