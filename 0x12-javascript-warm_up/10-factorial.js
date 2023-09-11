#!/usr/bin/node

function factorial(n) {
  return isNaN(n) || n < 0 ? 1 : n <= 1 ? 1 : n * factorial(n - 1);
}

const result = factorial(parseInt(process.argv[2]));
console.log(result);
