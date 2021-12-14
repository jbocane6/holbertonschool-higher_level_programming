#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments.
// You can assume all arguments can be converted to integer.
// If no argument passed, print 0.
// If the number of arguments is 1, print 0.
// You must use console.log(...) to print all output.
// You are not allowed to use var.
const { argv } = require('process');
const argc = argv.length - 2;
if (argc < 2) {
  console.log(0);
} else {
  const int_array = [];
  for (let i = 0; i < argc; i++) {
    int_array.push(parseInt(argv[i]));
  }
  int_array.sort((a, b) => a - b);
  console.log(int_array[argc - 2]);
}
