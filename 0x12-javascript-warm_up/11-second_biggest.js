#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.
// You can assume all arguments can be converted to integer.
// If no argument passed, print 0.
// If the number of arguments is 1, print 0.
// You must use console.log(...) to print all output.
// You are not allowed to use var.
let { argv } = require('process');
argv = argv.slice(2);
const argc = argv.length - 2;
if (argc < 2) {
  console.log(0);
} else {
  const intArray = [];
  for (let i = 0; i < argc; i++) {
    intArray.push(parseInt(argv[i]));
  }
  intArray.sort((a, b) => a - b);
  console.log(intArray[argc - 2]);
}
