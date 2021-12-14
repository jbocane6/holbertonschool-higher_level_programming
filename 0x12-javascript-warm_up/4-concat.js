#!/usr/bin/node
// Script that prints 2 arguments passed to it, in the following format: “ is ”
// You must use console.log(...) to print all output.
// You are not allowed to use var.
const { argv } = require('process');
if (argv[2] === undefined) {
  console.log('undefined is undefined');
} else {
  if (argv[3] === undefined) {
    console.log(argv[2] + ' is undefined');
  } else {
    console.log(argv[2] + ' is ' + argv[3]);
  }
}
