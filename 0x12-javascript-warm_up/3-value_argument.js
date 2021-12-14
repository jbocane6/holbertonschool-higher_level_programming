#!/usr/bin/node
// Script that prints the first argument passed to it.
// If no arguments are passed to the script, print “No argument”.
// You must use console.log(...) to print all output.
// You are not allowed to use var.
// You are not allowed to use length.
const { argv } = require('process');
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
