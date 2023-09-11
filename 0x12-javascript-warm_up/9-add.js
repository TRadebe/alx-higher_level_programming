#!/usr/bin/node

function add(a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    const result = a + b;
    console.log(result);
  } else {
    console.log('Invalid input. Please provide two valid numbers.');
  }
}

add(Number(process.argv[2]), Number(process.argv[3]));
