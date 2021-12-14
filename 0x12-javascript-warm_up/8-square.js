#!/usr/bin/node
// Script that prints a square.
// The first argument is the size of the square.
// If the first argument can’t be converted to an integer, print “Missing size”.
// You must use the character X to print the square.
// You must use console.log(...) to print all output.
// You are not allowed to use var.
// You must use a loop (while, for, etc.).
const { argv } = require('process');
const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing size');
} else if (num > 0) {
  const value = 'X';
  const row = Array.apply([], Array(num));
  row.forEach(() => console.log(value.repeat(num)));
}
