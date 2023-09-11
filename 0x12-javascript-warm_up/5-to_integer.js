#!/usr/bin/node

const firstArg = process.argv[2];

if (!isNaN(parseInt(firstArg))) {
  const convertedArg = parseInt(firstArg);
  console.log('My number:', convertedArg);
} else {
  console.log('Not a number');
}
